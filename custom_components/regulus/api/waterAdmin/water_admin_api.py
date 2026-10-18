from typing import Dict
from homeassistant.const import Platform

from ...schema import deviceSensor
from .water_admin_schemas import WaterAdminResponseSchema
from ...service.abstract_api import AbstractApi

class WaterAdminApi(AbstractApi[WaterAdminResponseSchema]):
    page = "/s_tv.xml"
    key = "waterAdmin"
    name = "Water Admin"

    def generate_response(self, schema_xml_map: Dict[str, str], registry_mapper: Dict[str, str]) -> WaterAdminResponseSchema:

        return WaterAdminResponseSchema(
            hotWaterTriggerOnDifference = deviceSensor("Water Trigger ON Diff", "hotWaterTriggerOnDifference", None, None, "mdi:arrow-up-bold-box-outline",
                                      Platform.NUMBER, schema_xml_map, registry_mapper),
        )
