from agent.initializer import agent
from utils.planner import write_plan

def run():
    task = "Guest Arrival Readiness"
    prompt = (
        "Prepare house for guest arrival: "
        "1. Turn on veranda and drawing room lights. "
        "2. Set living room temperature to 23°C. "
        "3. Unlock main gate and door. "
        "4. Start ceiling fans in drawing room. "
        "5. Activate air freshener. "
        "6. Light LED strip in puja room."
    )

    steps = [
        {
            "step_id": 1,
            "name": "Lighting Setup",
            "description": "Turn on lights in veranda and drawing room.",
            "reason": "Welcome guests with well-lit entrance.",
            "agent": "LightingAgent",
            "tool": "SmartLighting",
            "code": "set_light('veranda', 'bright_white', 90)",
            "input": {"room": "veranda", "color": "bright_white", "brightness": 90},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 2,
            "name": "Cool Living Room",
            "description": "Set AC to 23°C in living room.",
            "reason": "Comfort for incoming guests.",
            "agent": "ClimateAgent",
            "tool": "SmartAC",
            "code": "set_temperature('living_room', 23)",
            "input": {"room": "living_room", "temperature": 23},
            "output": {"temperature": 23},
            "state": {"before": {"temperature": 28}, "after": {"temperature": 23}}
        },
        {
            "step_id": 3,
            "name": "Unlock Entry",
            "description": "Unlock main gate and main door.",
            "reason": "Allow guest access.",
            "agent": "SecurityAgent",
            "tool": "SmartLockSystem",
            "code": "lock_doors(['main_gate', 'main_door'])",
            "input": {"doors": ["main_gate", "main_door"]},
            "output": {"locked": False},
            "state": {"before": {"main_gate": "locked", "main_door": "locked"}, "after": {"main_gate": "unlocked", "main_door": "unlocked"}}
        },
        {
            "step_id": 4,
            "name": "Start Fans",
            "description": "Turn on ceiling fans in drawing room.",
            "reason": "Maintain airflow.",
            "agent": "ApplianceAgent",
            "tool": "SmartFan",
            "code": "start_appliance('ceiling_fan', 'drawing_room')",
            "input": {"appliance_name": "ceiling_fan", "location": "drawing_room"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 5,
            "name": "Activate Air Freshener",
            "description": "Start fragrance device in hall.",
            "reason": "Make the atmosphere pleasant.",
            "agent": "ApplianceAgent",
            "tool": "SmartFragrance",
            "code": "start_appliance('air_freshener', 'hall')",
            "input": {"appliance_name": "air_freshener", "location": "hall"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 6,
            "name": "Decorative Lights",
            "description": "Light up LED strip in puja room.",
            "reason": "Enhance aesthetic.",
            "agent": "LightingAgent",
            "tool": "SmartLEDStrip",
            "code": "set_light('puja_room', 'amber', 100)",
            "input": {"room": "puja_room", "color": "amber", "brightness": 100},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        }
    ]

    write_plan(task, steps)
    agent.invoke(prompt)
