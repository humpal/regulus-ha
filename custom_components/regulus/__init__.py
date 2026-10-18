import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from datetime import timedelta

from .coordinator import RegulusUpdateCoordinator
from .api.dashboard.dashboard_api import DashboardApi
from .api.heatPump.heatPump_api import HeatPumpApi
from .api.heatPumpAdmin.heatPump_admin_api import HeatPumpAdminApi
from .api.home.home_api import HomeApi
from .api.water.water_api import WaterApi
from .api.waterAdmin.water_admin_api import WaterAdminApi
from .api.aku.aku_api import AkuApi
from .api.uniModule2.uni2_api import Uni2Api
from .api.zone1.zone1_api import Zone1Api
from .api.zone2.zone2_api import Zone2Api
from .api.zone3.zone3_api import Zone3Api
from .api.zone4.zone4_api import Zone4Api
from .api.zone5.zone5_api import Zone5Api
from .api.zone6.zone6_api import Zone6Api
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.NUMBER,
]

API_CLASSES = [
    AkuApi,
    DashboardApi,
    HeatPumpApi,
    HeatPumpAdminApi,
    HomeApi,
    WaterApi,
    WaterAdminApi,
    Uni2Api,
    Zone1Api,
    Zone2Api,
    Zone3Api,
    Zone4Api,
    Zone5Api,
    Zone6Api,
]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.info("SETUP: async_setup_entry called for %s", entry.entry_id)

    hass.data.setdefault(DOMAIN, {})

    entry.async_on_unload(
        entry.add_update_listener(async_reload_entry)
    )
    
    config = {
        "host": entry.options.get("ip_address", entry.data["ip_address"]),
        "user": entry.options.get("username", entry.data["username"]),
        "password": entry.options.get("password", entry.data["password"]),
        "ir_version": entry.options.get("ir_version", entry.data["ir_version"]),
        "polling_interval": timedelta(seconds=entry.options.get("polling_interval", entry.data["polling_interval"])),
    }
    
    coordinators: list[RegulusUpdateCoordinator] = []
    for api in API_CLASSES:
        option_key = f"enable_{api.key}"

        if not entry.options.get(option_key, True):
            _LOGGER.info("%s API disabled", api.key)
            continue

        try:
            api_instance = api(config)
            await hass.async_add_executor_job(api_instance.route_fetch)
            coordinator = RegulusUpdateCoordinator(hass, api_instance, scan_interval=config["polling_interval"])
            await coordinator.async_config_entry_first_refresh()
            coordinators.append(coordinator)
            _LOGGER.info("%s coordinator ready", api.name)

        except Exception as e:
            _LOGGER.error("Failed to setup %s API: %s", api.name, e)
        
    hass.data[DOMAIN][entry.entry_id] = {
        "coordinators": coordinators,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    _LOGGER.info("RELOAD: async_reload_entry called for %s", entry.entry_id)
    await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.info("UNLOAD: async_unload_entry called for %s", entry.entry_id)
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, PLATFORMS
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok    