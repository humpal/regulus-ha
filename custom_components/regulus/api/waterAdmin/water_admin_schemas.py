from pydantic import BaseModel

from ...schema import DeviceSchema

class WaterAdminResponseSchema(BaseModel):
    hotWaterTriggerOnDifference: DeviceSchema
