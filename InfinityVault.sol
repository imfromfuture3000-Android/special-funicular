// InfinityVault.sol
function distributeEarnings(uint total) internal {
  emit Reinvested(total * 60 / 100);
  emit Upgraded(total * 30 / 100);
  emit Airdropped(total * 10 / 100);
}
