from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone6_schemas import Zone6ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone6Api(AbstractApi[Zone6ResponseSchema]):
    page = "/zo_z6.xml"
    key = "zone6"
    name = "Zone 6"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone6ResponseSchema:

        return Zone6ResponseSchema(
            zone6State = deviceSensor("Zone 6 State", "zone6State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone6Temperature = deviceSensor("Zone 6 Temperature", "zone6Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone6DesiredTemperature = deviceSensor("Zone 6 Desired Temperature", "zone6DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
