import sys
import uuid
from pytradfri import Gateway
from pytradfri.device import Device
from pytradfri.api.libcoap_api import APIFactory

class LightApi:
    ip = "192.168.0.100"
    key = "7rX9YHWa64lcEjHp"
    gateway = Gateway()
    
    def __init__(self):
        identity = uuid.uuid4().hex

        api_factory = APIFactory(host=self.ip, psk_id=identity)

        api_factory.generate_psk(security_key=self.key)
        self.api = api_factory.request

    def get_all_lights(self):
        devices_command = self.gateway.get_devices()
        devices_commands = self.api(devices_command)
        devices = self.api(devices_commands)
        lights = [dev for dev in devices if dev.has_light_control]
        
        return lights

    def turn_on_light(self, light: Device):
        print("ON")
        dimmerValue = light.light_control.lights[0].dimmer
        self.api(light.light_control.set_dimmer(dimmerValue + 30))

    def turn_off_light(self, light: Device):
        print("OFF")
        dimmerValue = light.light_control.lights[0].dimmer

        self.api(light.light_control.set_dimmer(dimmer - 30))
