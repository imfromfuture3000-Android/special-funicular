
---

## 📄 `copilot-instruction.py`

```python
"""
🤖 copilot-instruction.py
Infinity Earnings Matrix — Autonomous Wealth Engine
"""

import os
from web3 import Web3
from biconomy import Biconomy
from elizaos import ElizaCore
from gnosis import GnosisSafe

# ————————————————
# CONFIG
# ————————————————

INFURA_RPC = f"https://linea-mainnet.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"
BICONOMY_KEY = os.getenv("BICONOMY_API_KEY")
w3 = Web3(Web3.HTTPProvider(INFURA_RPC))
biconomy = Biconomy(w3, api_key=BICONOMY_KEY)

# ————————————————
# AGENTS
# ————————————————

class Looter:
    def harvest(self):
        print("[Looter] Harvesting yield...")
        # Simulate tx
        return biconomy.sendGasless("Looter.harvest()")

class MEVMaster:
    def frontRun(self, pool):
        print("[MEV Master] Front-running...")
        return biconomy.sendPrivate("MEVMaster.execute()", pool)

class Arbitrader:
    def arbitrage(self, token):
        print("[Arbitrader] Cross-chain arb...")
        return biconomy.sendGasless("Arbitrader.execute()", token)

# ————————————————
# ORCHESTRATOR
# ————————————————

class AIOrchestrator:
    def __init__(self):
        self.agents = [Looter(), MEVMaster(), Arbitrader()]
        self.eliza = ElizaCore(model="iem-v1")

    def run(self):
        for agent in self.agents:
            if self.eliza.shouldRun(agent):
                agent.execute()

# ————————————————
# LAUNCH
# ————————————————

if __name__ == "__main__":
    bot = AIOrchestrator()
    bot.run()
