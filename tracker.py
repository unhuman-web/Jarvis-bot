import time
import requests
from friday import DataVault

def run_tracker():
    print("⏱️ Agent Tracker (The Pulse) Initialized.")
    while True:
        try:
            # Connects to price API or stream
            # Simulating live gold metrics updating into Friday's vault
            market = DataVault.read_vault().get("market_data", {})
            market["XAUUSD"] = {"price": 2425.50, "high": 2445.0, "low": 2405.0}
            DataVault.update_vault("market_data", market)
            
            print("[Tracker] Gold (XAUUSD) feed heartbeat synced to vault.")
            time.sleep(5)  # Quick 5-second pulse check
        except Exception as e:
            print(f"[Tracker Error] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_tracker()
