from agent.initializer import agent
from utils.planner import write_plan

def run():
    task = "Morning School Preparation"
    prompt = (
        "Morning school preparation: "
        "1. Start geyser in kids’ bathroom. "
        "2. Brighten lights in kids’ room. "
        "3. Start milk boiler and toaster. "
        "4. Turn on kitchen fan. "
        "5. Set bathroom temperature. "
        "6. Unlock front gate for school van."
    )

    steps = [
        {
            "step_id": 1,
            "name": "Start Geyser",
            "description": "Start geyser in kids' bathroom.",
            "reason": "Provide hot water for bathing.",
            "agent": "ApplianceAgent",
            "tool": "SmartApplianceController",
            "code": "start_appliance('geyser', 'kids_bathroom')",
            "input": {"appliance_name": "geyser", "location": "kids_bathroom"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 2,
            "name": "Brighten Lights",
            "description": "Set kids’ room lights to 70% brightness.",
            "reason": "Helps kids wake up gently.",
            "agent": "LightingAgent",
            "tool": "SmartLighting",
            "code": "set_light('kids_room', 'warm_white', 70)",
            "input": {"room": "kids_room", "color": "warm_white", "brightness": 70},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on", "color": "warm_white", "brightness": 70}}
        },
        {
            "step_id": 3,
            "name": "Start Breakfast Devices",
            "description": "Turn on milk boiler and toaster in kitchen.",
            "reason": "Prepare breakfast.",
            "agent": "ApplianceAgent",
            "tool": "SmartKitchen",
            "code": "start_appliance('milk_boiler', 'kitchen')",
            "input": {"appliance_name": "milk_boiler", "location": "kitchen"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 4,
            "name": "Ventilate Kitchen",
            "description": "Start fan in kitchen to remove cooking heat.",
            "reason": "Maintain air circulation.",
            "agent": "ApplianceAgent",
            "tool": "SmartFan",
            "code": "start_appliance('fan', 'kitchen')",
            "input": {"appliance_name": "fan", "location": "kitchen"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 5,
            "name": "Heat Bathroom",
            "description": "Set temperature in kids’ bathroom to 25°C.",
            "reason": "Make it comfortable for showering.",
            "agent": "ClimateAgent",
            "tool": "SmartThermostat",
            "code": "set_temperature('kids_bathroom', 25)",
            "input": {"room": "kids_bathroom", "temperature": 25},
            "output": {"temperature": 25},
            "state": {"before": {"temperature": 22}, "after": {"temperature": 25}}
        },
        {
            "step_id": 6,
            "name": "Unlock Front Gate",
            "description": "Unlock the front gate for school van.",
            "reason": "Allow pickup access.",
            "agent": "SecurityAgent",
            "tool": "SmartLock",
            "code": "lock_doors(['front_gate'])",
            "input": {"doors": ["front_gate"]},
            "output": {"locked": False},
            "state": {"before": {"front_gate": "locked"}, "after": {"front_gate": "unlocked"}}
        }
    ]

    write_plan(task, steps)
    agent.run(prompt)
