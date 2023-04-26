from phue import Bridge
from dotenv import load_dotenv
import os

load_dotenv()

HUE_BRIDGE_CONNECTION = Bridge(os.getenv("HUE_BRIDGE_IP"))
HUE_LIGHTS = HUE_BRIDGE_CONNECTION.lights


def switch_all_lights(command):
    case = "on" in command
    on_or_off = "on" if case else "off"
    for light in HUE_LIGHTS:
        light.on = case
    return f"Turning all lights {on_or_off}."


def switch_group_lights(command):
    case = "on" in command
    on_or_off = "on" if case else "off"
    HUE_BRIDGE_CONNECTION.set_group(1, "on", case)
    return f"Turning color lights {on_or_off}."


