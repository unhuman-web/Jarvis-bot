# scribe_investigator.py (Combined analytics scripts)
import time
from friday import DataVault

def run_analytics():
    print("✍️ Agent Scribe & 🔍 Investigator Operational.")
    while True:
        try:
            # Audit system logs and verify processing integrity
            vault = DataVault.read_vault()
            # Generate local analytics reports for Jarvis
            time.sleep(1800)
        except Exception as e:
            print(f"[Analytics Error] {e}")
            time.sleep(30)

if __name__ == "__main__":
    run_analytics()

