import json
import os

DB_FILE = "database.json"

class DataVault:
    @staticmethod
    def initialize_db():
        if not os.path.exists(DB_FILE):
            default_data = {
                "market_data": {"XAUUSD": {"price": 0.0, "high": 0.0, "low": 0.0}},
                "liquidity_pools": {"buy_side": [], "sell_side": []},
                "order_blocks": [],
                "fvgs": [],
                "active_trades": [],
                "agent_states": {}
            }
            with open(DB_FILE, 'w') as f:
                json.dump(default_data, f, indent=4)

    @staticmethod
    def read_vault():
        DataVault.initialize_db()
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    @staticmethod
    def update_vault(key, value):
        data = DataVault.read_vault()
        data[key] = value
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=4)
