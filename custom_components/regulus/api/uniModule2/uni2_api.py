from typing import Dict
from homeassistant.const import Platform
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.number import NumberDeviceClass

from ...schema import deviceSensor
from .uni2_schemas import Uni2ResponseSchema
from ...service.abstract_api import AbstractApi

class Uni2Api(AbstractApi[Uni2ResponseSchema]):
    page = "/s_na_m_2.xml"
    key = "uni2"
    name = "Uni Module 2"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> Uni2ResponseSchema:

        return Uni2ResponseSchema(
            uni2State = deviceSensor("Uni2 State", "uni2State", "", BinarySensorDeviceClass.RUNNING, "mdi:power",
                                      Platform.SWITCH, schema_xml_map, registry_mapper, converter=lambda v: v != "0"),
            uni2Temperature = deviceSensor("Uni2 Temperature", "uni2Temperature", "°C", SensorDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.SENSOR, schema_xml_map, registry_mapper),
            uni2DesiredTemperature = deviceSensor("Uni2 Desired Temperature", "uni2DesiredTemperature", "°C", NumberDeviceClass.TEMPERATURE, "mdi:thermometer",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
            uni2TriggerOnDiff = deviceSensor("Uni2 Triger ON Diff", "uni2TriggerOnDiff", "", None, "mdi:arrow-up-bold-box-outline",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
            uni2TriggerOffDiff = deviceSensor("Uni2 Triger OFF Diff", "uni2TriggerOffDiff", "", None, "mdi:arrow-down-bold-box-outline",
                                        Platform.NUMBER, schema_xml_map, registry_mapper),
        )
