import json
from datetime import datetime
import os

LOG_FILE = "logs/action_logs_india.json"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_action(entry):
    log = {
        "timestamp": datetime.now().isoformat(),
        "entry": entry
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log) + "\n")
