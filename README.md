## 🛡️ Why is it OWS Compatible?

This project is built strictly following the **Open Wallet Standard (OWS)** principles:

1. **Private Key Independence:** OWS Sentinel never requests or stores the user's Private Key or Seed Phrase. It operates as an external security layer that communicates with the wallet via OWS protocols.
2. **Identity & Agent Role:** By using the `Ows token create` logic, this agent acts as an **Authorized Representative**. It has specific permissions to "Analyze" and "Flag" transactions without having full control over the funds.
3. **Policy Enforcement:** The AI Risk Engine acts as a dynamic **Policy Provider**. 
   - **Low Risk:** Seamless OWS auto-approval.
   - **Medium Risk:** Triggers OWS manual confirmation request (Warning).
   - **High Risk:** Instant policy-based rejection to protect the wallet.
4. **Interoperability:** Designed to work with any wallet or dApp that adopts the Open Wallet Standard, ensuring a universal security layer for the Web3 ecosystem.
   
# 🛡️ OWS Sentinel

**AI-Powered Identity & Security Agent for the Open Wallet Standard (OWS)**

OWS Sentinel is an AI-driven security layer built on top of the Open Wallet Standard (OWS). It analyzes transactions in real-time and autonomously approves or blocks them without ever requiring the user's private key. Developed as a 1-day hackathon project.

## 🚀 Features

- **Advanced AI Risk Engine:** Scores transactions from 0 to 100 based on volume, velocity, target address reputation, and contract interaction types (e.g., risky "Approve" calls).
- **Autonomous Decision Making:** Silently auto-approves safe transactions via OWS, flags suspicious activities for manual review (Warning), and instantly blocks critical threats (e.g., blacklisted addresses).
- **Private Key Independence:** All authorizations are securely handled under the `my-agent-token` identity using OWS protocols.

## 🛠️ Installation & Setup

To run the simulation locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone [https://github.com/kozmosweb3/ows-sentinel.git](https://github.com/kozmosweb3/ows-sentinel.git)
````

2.  Install the required Python dependencies:
    ```bash
    pip install flask flask-cors
    ```
3.  Start the AI Backend server:
    ```bash
    python app.py
    ```
4.  Open the `index.html` file in your web browser to access the live simulation dashboard.

## 🔗 Developer & Contact

  - **Twitter:** [@kozmosweb3](https://www.google.com/search?q=https://twitter.com/kozmosweb3)

-----

*Built for the OWS Hackathon 🏆*

1. The Problem (30 Seconds)
"Web3 is still like the Wild West. Users are constantly terrified of signing malicious transactions or losing their private keys to phishing dApps. Current wallets either allow everything or block everything, with no intelligence in between."

2. The Solution: OWS Sentinel (40 Seconds)
"We built OWS Sentinel. It’s an AI-powered security agent that sits between the dApp and the wallet. Using the Open Wallet Standard (OWS), our agent analyzes every transaction request in real-time. It calculates a risk score from 0 to 100 based on behavioral patterns, blacklists, and contract anomalies."

3. Why OWS? (30 Seconds)
"The magic here is the Open Wallet Standard. OWS Sentinel functions as an Authorized Identity. It doesn't need your private key. It doesn't need your seed phrase. It simply provides a security 'verdict' to the wallet.

Low risk? Auto-approve via OWS.

Suspicious? Trigger a manual OWS confirmation.

Malicious? Instant block."

4. The Vision (20 Seconds)
"Our goal is to make Web3 as safe as a traditional bank account but without losing the decentralization. With OWS Sentinel, the AI protects you, while OWS keeps you in control. Thank you."
