import json
import os

def write_plan(task: str, steps: list):
    os.makedirs("plans", exist_ok=True)
    with open(f"plans/{task.lower().replace(' ', '_')}_plan.json", "w") as f:
        json.dump({"task": task, "plan": steps}, f, indent=4)
