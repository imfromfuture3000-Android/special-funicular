// Arbitrader.sol
function arbitrage(address token, uint amount) external onlyOrchestrator {
  uint profit = getArbProfit(token, amount);
  if (profit > ARB_MIN_PROFIT) {
    executeCrossChainArb(token, amount);
  }
}
