from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.binary_sensor import BinarySensorDeviceClass

from ...schema import deviceSensor
from .heatPump_admin_schemas import HeatPumpAdminResponseSchema
from ...service.abstract_api import AbstractApi

class HeatPumpAdminApi(AbstractApi[HeatPumpAdminResponseSchema]):
    page = "/s_zd_t.xml"
    key = "heatPumpAdmin"
    name = "Heat Pump Admin"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> HeatPumpAdminResponseSchema:

        return HeatPumpAdminResponseSchema(
            heatPumpPassiveCooling = deviceSensor("Heat Pump Passive Cooling", "heatPumpPassiveCooling", None, BinarySensorDeviceClass.RUNNING, "mdi:snowflake",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            heatPumpTriggerOnDifference = deviceSensor("Heat Pump Trigger ON Diff", "heatPumpTriggerOnDifference", None, None, "mdi:arrow-up-bold-box-outline",
                                      Platform.NUMBER, schema_xml_map, registry_mapper),
            heatPumpTriggerOffHysteresis = deviceSensor("Heat Pump Trigger OFF Diff", "heatPumpTriggerOffHysteresis", None, None, "mdi:arrow-down-bold-box-outline",
                                       Platform.NUMBER, schema_xml_map, registry_mapper),
        )