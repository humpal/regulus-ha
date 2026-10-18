from pydantic import BaseModel

from ...schema import DeviceSchema

class Uni2ResponseSchema(BaseModel):
    uni2State: DeviceSchema
    uni2Temperature: DeviceSchema
    uni2DesiredTemperature: DeviceSchema
    uni2TriggerOnDiff: DeviceSchema
    uni2TriggerOffDiff: DeviceSchema