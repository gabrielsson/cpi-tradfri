import sys
import uuid
import configparser
from pytradfri import Gateway
from pytradfri.device import Device
from pytradfri.api.libcoap_api import APIFactory
from typing import List
config = configparser.RawConfigParser()
config.read('tradfri.properties')

class LightApi:

    gateway = Gateway()
    
    def __init__(self):
        identity = uuid.uuid4().hex
        ##TODO: Fix all this with an on screen keyboard

        api_factory = APIFactory(host=config.get("TradfriSection", "ip"), psk_id=identity)

        api_factory.generate_psk(security_key=config.get("TradfriSection","key"))
        self.api = api_factory.request

    def get_all_lights(self):
        devices_command = self.gateway.get_devices()
        devices_commands = self.api(devices_command)
        devices = self.api(devices_commands)
        lights = [dev for dev in devices if dev.has_light_control]
        
        return lights

    def turn_on_light(self, light: Device):
        dimmerValue = light.light_control.lights[0].dimmer + 30
        self.api(light.light_control.set_dimmer(dimmerValue if dimmerValue < 254 else 254))
        deviceCommand = self.gateway.get_device(light.id)
        return self.api(deviceCommand)


    def turn_off_light(self, light: Device):
        dimmerValue = light.light_control.lights[0].dimmer - 30

        self.api(light.light_control.set_dimmer(dimmerValue if dimmerValue > 0 else 0))
        deviceCommand = self.gateway.get_device(light.id)

        return self.api(deviceCommand)