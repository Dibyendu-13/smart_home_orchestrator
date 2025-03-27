from agent.initializer import agent
from utils.planner import write_plan

def run():
    task = "Load Shedding Mode"
    prompt = (
        "Activate load shedding mode: "
        "1. Turn off non-essential appliances. "
        "2. Dim hallway and bedroom lights. "
        "3. Keep puja and kitchen lights on. "
        "4. Enable inverter mode. "
        "5. Turn off ACs, keep fans at medium. "
        "6. Lock all exterior doors."
    )

    steps = [
        {
            "step_id": 1,
            "name": "Turn Off Appliances",
            "description": "Shut down washing machine, TV, and microwave.",
            "reason": "Non-essential devices during power cut.",
            "agent": "ApplianceAgent",
            "tool": "SmartApplianceController",
            "code": "start_appliance('tv', 'living_room', status='off')",
            "input": {"appliance_name": "tv", "location": "living_room"},
            "output": {"status": "off"},
            "state": {"before": {"status": "on"}, "after": {"status": "off"}}
        },
        {
            "step_id": 2,
            "name": "Dim Lights",
            "description": "Dim hallway and bedroom lights to 20%.",
            "reason": "Save energy during outage.",
            "agent": "LightingAgent",
            "tool": "SmartLightingSystem",
            "code": "set_light('hallway', 'warm_white', 20)",
            "input": {"room": "hallway", "color": "warm_white", "brightness": 20},
            "output": {"status": "on"},
            "state": {"before": {"brightness": 100}, "after": {"brightness": 20}}
        },
        {
            "step_id": 3,
            "name": "Keep Essential Lights On",
            "description": "Ensure kitchen and puja room lights stay on.",
            "reason": "Maintain light where needed.",
            "agent": "LightingAgent",
            "tool": "SmartLightingSystem",
            "code": "set_light('puja_room', 'soft_white', 40)",
            "input": {"room": "puja_room", "color": "soft_white", "brightness": 40},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 4,
            "name": "Enable Inverter",
            "description": "Switch essential appliances to inverter backup.",
            "reason": "Sustain power supply for key appliances.",
            "agent": "ApplianceAgent",
            "tool": "SmartInverter",
            "code": "start_appliance('inverter_mode', 'main_panel')",
            "input": {"appliance_name": "inverter_mode", "location": "main_panel"},
            "output": {"status": "on"},
            "state": {"before": {"inverter": "off"}, "after": {"inverter": "on"}}
        },
        {
            "step_id": 5,
            "name": "Turn Off ACs",
            "description": "Switch off all air conditioners, keep ceiling fans on medium speed.",
            "reason": "Prevent power overload.",
            "agent": "ApplianceAgent",
            "tool": "SmartClimateControl",
            "code": "start_appliance('fan', 'bedroom', speed='medium')",
            "input": {"appliance_name": "fan", "location": "bedroom", "speed": "medium"},
            "output": {"status": "on"},
            "state": {"before": {"speed": "high"}, "after": {"speed": "medium"}}
        },
        {
            "step_id": 6,
            "name": "Lock Exterior Doors",
            "description": "Lock main gate, backyard, and balcony doors.",
            "reason": "Ensure security during power outage.",
            "agent": "SecurityAgent",
            "tool": "SmartLockSystem",
            "code": "lock_doors(['main_gate', 'backyard', 'balcony'])",
            "input": {"doors": ["main_gate", "backyard", "balcony"]},
            "output": {"locked": True},
            "state": {
                "before": {"main_gate": "unlocked", "backyard": "unlocked", "balcony": "unlocked"},
                "after": {"main_gate": "locked", "backyard": "locked", "balcony": "locked"}
            }
        }
    ]

    write_plan(task, steps)
    agent.invoke(prompt)
