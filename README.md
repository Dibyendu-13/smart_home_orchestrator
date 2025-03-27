# 🏠 Smart Home Multi-Agent Orchestrator

An intelligent, modular home automation framework powered by **LangChain agents**, **LLMs**, and **StructuredTool** interfaces for controlling lighting, appliances, climate, and security in a modern smart home.

Supports structured routines like:

- 🕯 Evening Relaxation Setup  
- 🌅 Morning School Preparation  
- 👋 Guest Arrival Readiness  
- ⚡ Load Shedding Power-Save Mode  
- 🚪 Leaving Home Routine  

---

## 📦 Features

✅ Multi-agent home automation system  
✅ Modular task planning via JSON plans  
✅ LLM-powered command execution with reasoning  
✅ Transparent action logging with state tracking  
✅ Extensible: add your own tools, routines, or devices

---

## 🧠 Project Structure

```

smart_home_orchestrator/
├── main.py                         # Entry point: runs all tasks
├── agent/
│   ├── initializer.py              # Sets up LLM and LangChain tools
│   ├── tools.py                    # Tool logic for agents (StructuredTool)
│   └── logger.py                   # JSON-based logger with before/after state
├── tasks/
│   ├── evening_relaxation.py      # Lighting + AC + appliance setup
│   ├── morning_school_prep.py     # Geyser, kitchen, fan, lights
│   ├── guest_arrival.py           # Lighting, fragrance, cooling
│   ├── load_shedding.py           # Dims + inverter + security
│   └── leaving_home.py            # Full shutdown with surveillance mode
├── utils/
│   └── planner.py                 # JSON plan generation for each task
├── plans/
│   └── *.json                     # Auto-generated step-by-step plans
├── logs/
│   └── action_logs.json           # Action execution logs
└── .env                           # Environment variables (e.g. API key)

```

---

## 🚀 Getting Started

### 1️⃣ Install Requirements

```bash
git clone https://github.com/Dibyendu-13/smart_home_orchestrator.git
cd smart_home_orchestrator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Configure API Key

```bash
touch .env
```

Paste this:

```
OPENAI_API_KEY=sk-yourkeyhere
```

---

## ▶️ Run the Automation

```bash
python main.py
```

All tasks will be executed one after the other.  
You’ll see terminal output + generated plans (`/plans`) and logs (`/logs`).

---

## 🤖 Agents & Their Capabilities

| Agent Name       | Tool Used         | Functionality                           |
|------------------|-------------------|-----------------------------------------|
| `LightingAgent`  | `set_light`       | Adjusts room lighting color/brightness  |
| `ClimateAgent`   | `set_temperature` | Controls room temperature               |
| `SecurityAgent`  | `lock_doors`      | Locks specified doors                   |
| `ApplianceAgent` | `start_appliance` | Turns on/off appliances (TV, fan, etc.) |

---

## 🗓 Task Routines Included

### 🕯 Evening Relaxation

1. Set lights to warm yellow (60%) in living area  
2. Turn off TV/music systems  
3. Start diffuser for fragrance  
4. Reduce ceiling fan speed  
5. Set temperature to 26°C  
6. Lock balcony and back gate  

### 🌅 Morning School Prep

1. Start geyser in bathroom  
2. Brighten bedroom lights  
3. Start milk boiler and toaster  
4. Ventilate kitchen with fan  
5. Set bathroom to 24°C  
6. Lock front gate for safety  

### 👋 Guest Arrival Setup

1. Turn on drawing room, veranda lights  
2. Cool living room with AC (23°C)  
3. Start fans in drawing room  
4. Turn on fragrance dispenser  
5. Light decorative LED  
6. [Manual] Unlock front door if needed  

### ⚡ Load Shedding Mode

1. Turn off high-energy appliances  
2. Dim lights in non-critical areas  
3. Enable inverter for essentials  
4. Turn off ACs, use fans  
5. Lock all external doors  

### 🚪 Leaving Home Routine

1. Turn off lights and fans  
2. Power down appliances  
3. Set ACs to standby  
4. Lock all doors and gates  
5. Turn on porch security light  
6. Activate surveillance mode  

---

## 📊 Logs

Each executed step is logged in `logs/action_logs.json` including:

- ✅ Agent used
- 🧠 Action + tool description
- 🟨 Input & output
- 🟩 State before and after
- 📅 Timestamp

---

## 🛠 Built With

- Python 🐍  
- LangChain Agents & Tools  
- OpenAI GPT-4 API  
- Pydantic for input validation  
- JSON for plan & state structure  

---

## 📌 Future Enhancements

- 🗣 Voice command integration  
- 📲 Web interface to trigger tasks  
- 🧠 Add memory for preferences (e.g., bedroom fan speed)  
- 🔐 Facial recognition for door locks  
- 🌐 IoT MQTT / Zigbee integration for real-world devices  

---



