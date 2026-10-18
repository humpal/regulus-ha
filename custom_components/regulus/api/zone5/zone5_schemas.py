from pydantic import BaseModel

from ...schema import DeviceSchema

class Zone5ResponseSchema(BaseModel):
    zone5State: DeviceSchema
    zone5CoolingState: DeviceSchema
    zone5Temperature: DeviceSchema
    zone5DesiredTemperature: DeviceSchema
    zone5Humidity: DeviceSchema
    zone5HeatingWaterTemperature: DeviceSchema
    zone5RequiredHeatingWaterTemperature: DeviceSchema