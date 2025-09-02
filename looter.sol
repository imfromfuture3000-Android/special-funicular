// Looter.sol
function harvestAll() external onlyOrchestrator {
  for (uint i = 0; i < farms.length; i++) {
    farms[i].harvest();
    reinvest(farms[i].rewards());
  }
}
