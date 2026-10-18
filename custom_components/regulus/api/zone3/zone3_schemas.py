from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone3ResponseSchema(BaseModel):
    zone3State: DeviceSchema
    zone3Temperature: DeviceSchema
    zone3DesiredTemperature: DeviceSchema