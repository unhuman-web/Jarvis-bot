import os
import sys
import time
import subprocess
import threading
import requests
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "⚡ JARVIS MAIN COMMAND CENTER: 100% OPERATIONAL."

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

TELEGRAM_TOKEN = "8665339589:AAFe9iEHbndBkgw0swsbtsJx432C4AHo77Q"
CHAT_ID = "6237872126"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
    except Exception:
        pass

def manage_agents():
    print("🤖 JARVIS: Initiating multi-agent subprocess cluster...")
    send_to_telegram("⚡ JARVIS CORE ONLINE: Deploying autonomous modular processes for Vision, Tracker, Rex, Friday, and Analytics...")
    
    # Absolute paths to individual agent scripts
    agents = {
        "Vision (Scraper)": [sys.executable, "vision.py"],
        "Tracker (Pulse)": [sys.executable, "tracker.py"],
        "Rex (Executor)": [sys.executable, "rex.py"],
        "Analytics Team": [sys.executable, "scribe_investigator.py"]
    }
    
    running_processes = {}
    
    # Spawn each agent as an independent process
    for agent_name, command in agents.items():
        try:
            proc = subprocess.Popen(command)
            running_processes[agent_name] = proc
            print(f"✅ Launched {agent_name} process lane [PID: {proc.pid}]")
        except Exception as e:
            send_to_telegram(f"❌ Jarvis failed to initiate agent process: {agent_name}. Error: {e}")

    # Jarvis dynamic supervisory controller loop
    while True:
        time.sleep(30)
        for agent_name, proc in running_processes.items():
            poll = proc.poll()
            if poll is not None:  # Process has crashed or stopped
                send_to_telegram(f"⚠️ JARVIS CONTROL WARNING: {agent_name} dropped execution. Attempting immediate process recovery...")
                print(f"[Jarvis Supervisor] Restoring collapsed lane for: {agent_name}")
                new_proc = subprocess.Popen(agents[agent_name])
                running_processes[agent_name] = new_proc
                send_to_telegram(f"✅ JARVIS: {agent_name} process recovery sequence successful.")

if __name__ == "__main__":
    # Start web container thread
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Start Jarvis supervisory array
    manage_agents()

