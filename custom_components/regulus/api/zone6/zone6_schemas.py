from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone6ResponseSchema(BaseModel):
    zone6State: DeviceSchema
    zone6Temperature: DeviceSchema
    zone6DesiredTemperature: DeviceSchema