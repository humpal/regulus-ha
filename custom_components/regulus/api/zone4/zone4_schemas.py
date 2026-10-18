from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone4ResponseSchema(BaseModel):
    zone4State: DeviceSchema
    zone4Temperature: DeviceSchema
    zone4DesiredTemperature: DeviceSchema