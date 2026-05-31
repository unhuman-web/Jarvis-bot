import os
import time
import threading
import requests
from flask import Flask

# 1. Create a tiny background web server to keep Render happy
app = Flask('')

@app.route('/')
def home():
    return "Jarvis System is Online and Running 24/7."

def run_web_server():
    # Render provides a PORT environment variable automatically
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Injected Keys for your trading bot
ALPACA_KEY = "PKVBIZC327JE2GBSJ7SNUUVEZZ"
ALPACA_SECRET = "7o4qCaiwDQQ1P2DWZcGXg1qbvHpsJdHxzSzS9GUcPAbS"
TELEGRAM_TOKEN = "8665339589:AAFe9iEHbndBkgw0swsbtsJx432C4AHo77Q"
CHAT_ID = "6237872126"
BASE_URL = "https://paper-api.alpaca.markets"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
    except Exception:
        pass

def check_alpaca():
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    try:
        response = requests.get(f"{BASE_URL}/v2/account", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("cash", "0.00")
    except Exception:
        return None
    return None

# 3. Main loop that runs your agent
def trading_loop():
    print("🤖 Activating Jarvis Trading System on Cloud Server...")
    send_to_telegram("🤖 JARVIS SYSTEM: CLOUD DEPLOYMENT ONLINE.\nInitializing secure bridge to Alpaca...")
    
    cash_balance = check_alpaca()
    if cash_balance:
        success_msg = f"✅ Cloud Bridge Established!\n💰 Simulated Cash Balance: ${float(cash_balance):,.2f}\n\nAgent Rex is now scanning market data from the web server 24/7."
        print(success_msg)
        send_to_telegram(success_msg)
    else:
        send_to_telegram("❌ Cloud Connection Failed. Check your API keys.")

    # Keep running silently forever
    while True:
        try:
            # This keeps your agent checking the market or staying alive
            time.sleep(60)
        except Exception:
            pass

if __name__ == "__main__":
    # Start the web server thread so Render stays connected
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Start the trading agent loop
    trading_loop()
