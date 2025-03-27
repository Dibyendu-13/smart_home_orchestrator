from agent.initializer import agent
from utils.planner import write_plan

def run():
    task = "Leaving for Office"
    prompt = (
        "Leaving for work routine: "
        "1. Turn off all lights and fans. "
        "2. Shut down geyser and induction. "
        "3. Set all ACs to standby at 28°C. "
        "4. Lock all doors and main gate. "
        "5. Turn on porch security light. "
        "6. Activate surveillance mode."
    )

    steps = [
        {
            "step_id": 1,
            "name": "Switch Off Devices",
            "description": "Turn off all fans and lights across the house.",
            "reason": "Energy conservation while away.",
            "agent": "LightingAgent",
            "tool": "SmartLightingSystem",
            "code": "set_light('all_rooms', 'off', 0)",
            "input": {"room": "all_rooms", "color": "none", "brightness": 0},
            "output": {"status": "off"},
            "state": {"before": {"status": "on"}, "after": {"status": "off"}}
        },
        {
            "step_id": 2,
            "name": "Turn Off High Power Appliances",
            "description": "Geyser and induction off in bathroom and kitchen.",
            "reason": "Safety precaution while away.",
            "agent": "ApplianceAgent",
            "tool": "SmartPowerSwitch",
            "code": "start_appliance('geyser', 'bathroom', status='off')",
            "input": {"appliance_name": "geyser", "location": "bathroom"},
            "output": {"status": "off"},
            "state": {"before": {"status": "on"}, "after": {"status": "off"}}
        },
        {
            "step_id": 3,
            "name": "Set ACs to Standby",
            "description": "Put ACs in all rooms to standby at 28°C.",
            "reason": "Maintain ambient temperature and save power.",
            "agent": "ClimateAgent",
            "tool": "SmartAC",
            "code": "set_temperature('all_rooms', 28)",
            "input": {"room": "all_rooms", "temperature": 28},
            "output": {"temperature": 28},
            "state": {"before": {"temperature": 24}, "after": {"temperature": 28}}
        },
        {
            "step_id": 4,
            "name": "Lock Everything",
            "description": "Lock all doors including main gate and side exit.",
            "reason": "House security.",
            "agent": "SecurityAgent",
            "tool": "SmartLockSystem",
            "code": "lock_doors(['main_door', 'main_gate', 'side_exit'])",
            "input": {"doors": ["main_door", "main_gate", "side_exit"]},
            "output": {"locked": True},
            "state": {
                "before": {"main_door": "unlocked", "main_gate": "unlocked", "side_exit": "unlocked"},
                "after": {"main_door": "locked", "main_gate": "locked", "side_exit": "locked"}
            }
        },
        {
            "step_id": 5,
            "name": "Security Light",
            "description": "Turn on 40% brightness security light in porch.",
            "reason": "Evening visibility and safety.",
            "agent": "LightingAgent",
            "tool": "SmartSecurityLight",
            "code": "set_light('porch', 'cool_white', 40)",
            "input": {"room": "porch", "color": "cool_white", "brightness": 40},
            "output": {"status": "on"},
            "state": {"before": {"status": "off"}, "after": {"status": "on"}}
        },
        {
            "step_id": 6,
            "name": "Activate Surveillance",
            "description": "Enable full surveillance mode.",
            "reason": "24x7 camera recording while away.",
            "agent": "ApplianceAgent",
            "tool": "SmartSecuritySystem",
            "code": "start_appliance('surveillance', 'main_panel')",
            "input": {"appliance_name": "surveillance", "location": "main_panel"},
            "output": {"status": "active"},
            "state": {"before": {"status": "off"}, "after": {"status": "active"}}
        }
    ]

    write_plan(task, steps)
    agent.invoke(prompt)
