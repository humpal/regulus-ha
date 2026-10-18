from pydantic import BaseModel
from ...schema import DeviceSchema

class HeatPumpAdminResponseSchema(BaseModel):
    heatPumpTriggerOnDifference: DeviceSchema
    heatPumpTriggerOffHysteresis: DeviceSchema
    heatPumpPassiveCooling: DeviceSchema