// MEVMaster.sol
function frontRun(address pool, uint profit) external onlyOrchestrator {
  if (profit > MEV_MIN_PROFIT) {
    executeViaSUAVE(pool, profit);
  }
}
