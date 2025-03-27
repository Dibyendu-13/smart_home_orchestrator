from langchain.tools import StructuredTool
from pydantic import BaseModel
from agent.logger import log_action


# Lighting Tool

class SetLightInput(BaseModel):
    room: str
    color: str
    brightness: int

def set_light(room: str, color: str, brightness: int) -> dict:
    result = {
        "agent": "LightingAgent",
        "action": f"Set light in {room} to {color} at {brightness}%",
        "state": {
            "before": {"status": "off"},
            "after": {"status": "on", "color": color, "brightness": brightness}
        }
    }
    log_action(result)
    return result

set_light_tool = StructuredTool.from_function(
    func=set_light,
    name="set_light",
    description="Set lighting in a room by specifying room, color, and brightness."
)


# Climate Tool

class SetTemperatureInput(BaseModel):
    room: str
    temperature: float

def set_temperature(room: str, temperature: float) -> dict:
    result = {
        "agent": "ClimateAgent",
        "action": f"Set temperature in {room} to {temperature}°C",
        "state": {
            "before": {"temperature": "unknown"},
            "after": {"temperature": temperature}
        }
    }
    log_action(result)
    return result

set_temperature_tool = StructuredTool.from_function(
    func=set_temperature,
    name="set_temperature",
    description="Set room temperature. Provide room name and desired temperature in °C."
)


# Security Tool

class LockDoorsInput(BaseModel):
    doors: list[str]

def lock_doors(doors: list[str]) -> dict:
    result = {
        "agent": "SecurityAgent",
        "action": f"Locked doors: {', '.join(doors)}",
        "state": {
            "before": {d: "unlocked" for d in doors},
            "after": {d: "locked" for d in doors}
        }
    }
    log_action(result)
    return result

lock_doors_tool = StructuredTool.from_function(
    func=lock_doors,
    name="lock_doors",
    description="Lock specified doors. Provide a list of door names."
)


# Appliance Tool

class StartApplianceInput(BaseModel):
    appliance_name: str
    location: str

def start_appliance(appliance_name: str, location: str) -> dict:
    result = {
        "agent": "ApplianceAgent",
        "action": f"Started {appliance_name} in {location}",
        "state": {
            "before": {"status": "off"},
            "after": {"status": "on"}
        }
    }
    log_action(result)
    return result

start_appliance_tool = StructuredTool.from_function(
    func=start_appliance,
    name="start_appliance",
    description="Start a named appliance in a specific location."
)
