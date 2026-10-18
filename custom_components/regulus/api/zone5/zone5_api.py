from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .zone5_schemas import Zone5ResponseSchema
from ...service.abstract_api import AbstractApi

class Zone5Api(AbstractApi[Zone5ResponseSchema]):
    page = "/zo_z5.xml"
    key = "zone5"
    name = "Zone 5"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Zone5ResponseSchema:

        return Zone5ResponseSchema(
            zone5State = deviceSensor("Zone 5 State", "zone5State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone5CoolingState = deviceSensor("Zone 5 Cooling State", "zone5CoolingState", "", BinarySensorDeviceClass.RUNNING, "mdi:snowflake",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            zone5Temperature = deviceSensor("Zone 5 Temperature", "zone5Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone5DesiredTemperature = deviceSensor("Zone 5 Desired Temperature", "zone5DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
            zone5Humidity = deviceSensor("Zone 5 Humidity", "zone5Humidity", "%", SensorDeviceClass.HUMIDITY, "mdi:water-percent",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone5HeatingWaterTemperature = deviceSensor("Zone 5 Water Temperature", "zone5HeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            zone5RequiredHeatingWaterTemperature = deviceSensor("Zone 5 Required Water Temperature", "zone5RequiredHeatingWaterTemperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
        )
