from flask import Flask, jsonify
from flask_cors import CORS
import random
import hashlib
import time

app = Flask(__name__)
CORS(app)

# Corporate AI Agents and Budget Policies
AGENTS = {
    "AGENT_MARKETING": {
        "wallet_name": "agent-marketing", 
        "daily_limit": 50.0, 
        "spent_today": 42.0, 
        "allowed_vendors": ["0xTwitterAds", "0xStableStudio"]
    },
    "AGENT_RESEARCH": {
        "wallet_name": "agent-research", 
        "daily_limit": 5.0, 
        "spent_today": 1.5, 
        "allowed_vendors": ["0xFirecrawl_API", "0xDeepSeek"]
    },
    "AGENT_TRADER": {
        "wallet_name": "agent-trader", 
        "daily_limit": 500.0, 
        "spent_today": 480.0, 
        "allowed_vendors": ["0xUniswapRouter", "0xAavePool"]
    }
}

def simulate_ows_cli_sign(wallet_name, target_address, amount):
    """
    Hackathon Magic: Simulates OWS CLI which is currently unavailable on Windows.
    Generates a realistic AES-256 style hash to mimic local vault encryption.
    """
    time.sleep(0.5) # Simulate CLI execution time
    
    # Generate mock cryptographic signature
    raw_data = f"{wallet_name}-{target_address}-{amount}-{time.time()}"
    fake_signature = "0x" + hashlib.sha256(raw_data.encode()).hexdigest()
    
    return {
        "status": "APPROVED", 
        "reason": "Signed Locally via OWS Vault", 
        "signature": fake_signature
    }

def check_spend_policy_and_execute(agent_id, vendor, amount):
    """Checks SpendOS Policy, if passed, sends to OWS Signature engine."""
    agent = AGENTS.get(agent_id)
    
    # 1. Vendor (Target) Check
    if vendor not in agent["allowed_vendors"]:
        return {"status": "BLOCKED", "reason": f"Unauthorized Target: {vendor}"}

    # 2. Daily Budget Limit Check
    if agent["spent_today"] + amount > agent["daily_limit"]:
        return {"status": "BLOCKED", "reason": f"Budget Exceeded! (Max: {agent['daily_limit']} USDC)"}

    # 3. Policy Passed -> Send to OWS CLI Simulator
    ows_result = simulate_ows_cli_sign(agent["wallet_name"], vendor, amount)
    
    if ows_result["status"] == "APPROVED":
        agent["spent_today"] += amount
        ows_result["reason"] += f" | Remaining: {(agent['daily_limit'] - agent['spent_today']):.2f}"
        
    return ows_result

@app.route('/api/simulate_tx', methods=['GET'])
def simulate_tx():
    """Endpoint triggered by the frontend to simulate a transaction."""
    agent_ids = list(AGENTS.keys())
    selected_agent = random.choice(agent_ids)
    
    # Mix allowed vendors with an unauthorized one for demonstration
    vendors = AGENTS[selected_agent]["allowed_vendors"] + ["0xUnknownHackerWallet"]
    selected_vendor = random.choice(vendors)
    amount = round(random.uniform(1.0, 10.0), 2)
    
    tx_data = {
        "id": f"OWS-{random.randint(10000, 99999)}",
        "agent": AGENTS[selected_agent]["wallet_name"],
        "vendor": selected_vendor,
        "amount": amount,
        "asset": "USDC"
    }

    # Execute core policy engine
    policy_result = check_spend_policy_and_execute(selected_agent, selected_vendor, amount)
    tx_data.update(policy_result)
    
    return jsonify(tx_data)

if __name__ == '__main__':
    print("💼 OWS SpendOS - DEMO MODE ACTIVE (Windows Fallback),")
    app.run(debug=True, port=5000)