import sys
import uuid
import configparser
from pytradfri import Gateway
from pytradfri.device import Device
from pytradfri.api.libcoap_api import APIFactory
from typing import List
  
def api_factory():
    identity = uuid.uuid4().hex
    ##TODO: Fix all this with an on screen keyboard
    config = configparser.RawConfigParser()
    config.read('tradfri.properties')
    api_factory = APIFactory(host=config.get("TradfriSection", "ip"), psk_id=identity)

    api_factory.generate_psk(security_key=config.get("TradfriSection","key"))
    return api_factory.request

api = api_factory()
gateway = Gateway()

def get_all_lights():
    devices_command = gateway.get_devices()
    devices_commands = api(devices_command)
    devices = api(devices_commands)
    lights = [dev for dev in devices if dev.has_light_control]
    
    return lights

def turn_on_light(light: Device):
    dimmerValue = light.light_control.lights[0].dimmer + 30
    api(light.light_control.set_dimmer(dimmerValue if dimmerValue < 254 else 254))
    deviceCommand = gateway.get_device(light.id)
    return api(deviceCommand)


def turn_off_light(light: Device):
    dimmerValue = light.light_control.lights[0].dimmer - 30

    api(light.light_control.set_dimmer(dimmerValue if dimmerValue > 0 else 0))
    deviceCommand = gateway.get_device(light.id)

    return api(deviceCommand)