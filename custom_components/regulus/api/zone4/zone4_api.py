from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone4_schemas import Zone4ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone4Api(AbstractApi[Zone4ResponseSchema]):
    page = "/zo_z4.xml"
    key = "zone4"
    name = "Zone 4"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone4ResponseSchema:

        return Zone4ResponseSchema(
            zone4State = deviceSensor("Zone 4 State", "zone4State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone4Temperature = deviceSensor("Zone 4 Temperature", "zone4Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone4DesiredTemperature = deviceSensor("Zone 4 Desired Temperature", "zone4DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
