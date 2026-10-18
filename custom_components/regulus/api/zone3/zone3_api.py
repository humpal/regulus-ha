from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone3_schemas import Zone3ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone3Api(AbstractApi[Zone3ResponseSchema]):
    page = "/zo_z3.xml"
    key = "zone3"
    name = "Zone 3"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone3ResponseSchema:

        return Zone3ResponseSchema(
            zone3State = deviceSensor("Zone 3 State", "zone3State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone3Temperature = deviceSensor("Zone 3 Temperature", "zone3Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone3DesiredTemperature = deviceSensor("Zone 3 Desired Temperature", "zone3DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
