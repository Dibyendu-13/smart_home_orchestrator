from agent.initializer import agent
from utils.planner import write_plan

def run():
    task = "Evening Puja Preparation"
    prompt = (
        "Evening puja preparation: "
        "1. Set warm yellow light in puja room at 60% brightness. "
        "2. Turn off all entertainment systems like TV and music. "
        "3. Start incense diffuser in puja room. "
        "4. Set ceiling fan in puja room to low. "
        "5. Adjust AC to 26°C in puja room. "
        "6. Lock balcony and back gate for privacy."
    )

    steps = [
        {
            "step_id": 1,
            "name": "Puja Light",
            "description": "Set warm yellow light in puja room at 60%",
            "reason": "Creates a peaceful spiritual setting.",
            "agent": "LightingAgent",
            "tool": "SmartLightingSystem",
            "code": "set_light({'room': 'puja_room', 'color': 'warm_yellow', 'brightness': 60})",
            "input": {"room": "puja_room", "color": "warm_yellow", "brightness": 60},
            "output": {"status": "on"},
            "state": {
                "before": {"status": "off"},
                "after": {"status": "on", "color": "warm_yellow", "brightness": 60}
            }
        },
        {
            "step_id": 2,
            "name": "Turn off Entertainment",
            "description": "Turn off TV and music in the living room.",
            "reason": "Maintain quiet and focus during puja.",
            "agent": "ApplianceAgent",
            "tool": "SmartApplianceController",
            "code": "start_appliance({'appliance_name': 'tv', 'location': 'living_room', 'status': 'off'})",
            "input": {"appliance_name": "tv", "location": "living_room", "status": "off"},
            "output": {"status": "off"},
            "state": {"before": {"status": "on"}, "after": {"status": "off"}}
        },
        {
            "step_id": 3,
            "name": "Start Incense Diffuser",
            "description": "Start the incense diffuser to release fragrance.",
            "reason": "Enhance spiritual ambiance with aroma.",
            "agent": "ApplianceAgent",
            "tool": "SmartDiffuser",
            "code": "start_appliance({'appliance_name': 'incense_diffuser', 'location': 'puja_room'})",
            "input": {"appliance_name": "incense_diffuser", "location": "puja_room"},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 4,
            "name": "Reduce Fan Speed",
            "description": "Reduce the ceiling fan speed in puja room to low.",
            "reason": "Prevent airflow disturbance to diyas and incense.",
            "agent": "ApplianceAgent",
            "tool": "SmartFan",
            "code": "start_appliance({'appliance_name': 'ceiling_fan', 'location': 'puja_room', 'speed': 'low'})",
            "input": {"appliance_name": "ceiling_fan", "location": "puja_room", "speed": "low"},
            "output": {"status": "on", "speed": "low"},
            "state": {"before": {"speed": "medium"}, "after": {"speed": "low"}}
        },
        {
            "step_id": 5,
            "name": "Set Room Temperature",
            "description": "Set AC in puja room to 26°C for comfort.",
            "reason": "Keep temperature balanced and comfortable.",
            "agent": "ClimateAgent",
            "tool": "SmartThermostat",
            "code": "set_temperature({'room': 'puja_room', 'temperature': 26})",
            "input": {"room": "puja_room", "temperature": 26},
            "output": {"temperature": 26},
            "state": {"before": {"temperature": 28}, "after": {"temperature": 26}}
        },
        {
            "step_id": 6,
            "name": "Lock Doors",
            "description": "Lock balcony and back gate for privacy and security.",
            "reason": "Prevent disturbances during the ritual.",
            "agent": "SecurityAgent",
            "tool": "SmartLockSystem",
            "code": "lock_doors({'doors': ['balcony', 'back_gate']})",
            "input": {"doors": ["balcony", "back_gate"]},
            "output": {"locked": True},
            "state": {
                "before": {"balcony": "unlocked", "back_gate": "unlocked"},
                "after": {"balcony": "locked", "back_gate": "locked"}
            }
        }
    ]

    write_plan(task, steps)
    agent.run(prompt)
