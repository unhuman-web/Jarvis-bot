import time
import requests
from friday import DataVault

ALPACA_KEY = "PKVBIZC327JE2GBSJ7SNUUVEZZ"
ALPACA_SECRET = "7o4qCaiwDQQ1P2DWZcGXg1qbvHpsJdHxzSzS9GUcPAbS"
BASE_URL = "https://paper-api.alpaca.markets"

def run_rex():
    print("🦈 Agent Rex (SMC/ICT Trading Engine) Initialized.")
    headers = {"APCA-API-KEY-ID": ALPACA_KEY, "APCA-API-SECRET-KEY": ALPACA_SECRET}
    
    while True:
        try:
            vault = DataVault.read_vault()
            current_price = vault.get("market_data", {}).get("XAUUSD", {}).get("price", 0)
            buy_liquidity = vault.get("liquidity_pools", {}).get("buy_side", [])
            
            # ICT Framework Verification: Checking if price swept buy-side liquidity
            if buy_liquidity and current_price >= max(buy_liquidity):
                print("[Rex] Liquidity Sweep Identified! Waiting for structural shift validation...")
                # Execution logic for order placement goes here via Alpaca API requests
                
            time.sleep(10)
        except Exception as e:
            print(f"[Rex Error] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_rex()
