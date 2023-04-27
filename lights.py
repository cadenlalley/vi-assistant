from phue import Bridge
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()
HUE_BRIDGE_CONNECTION = Bridge(os.getenv("HUE_BRIDGE_IP"))
HUE_LIGHTS = HUE_BRIDGE_CONNECTION.lights


"""Turn all of your Philips Hue Lights on or off.
:param command: command that specifies lights on or off.
:returns: string to be spoken by TTS engine.
"""
def switch_all_lights(command):
    case = "on" in command
    on_or_off = "on" if case else "off"
    for light in HUE_LIGHTS:
        light.on = case
    return f"Turning all lights {on_or_off}."


"""This is a function that is specific to my personal use. Switches a group of my lights on or off.
:param command: command that specifies lights on or off.
:returns: string to be spoken by TTS engine.
"""
def switch_group_lights(command):
    case = "on" in command
    on_or_off = "on" if case else "off"
    HUE_BRIDGE_CONNECTION.set_group(1, "on", case)
    return f"Turning color lights {on_or_off}."


