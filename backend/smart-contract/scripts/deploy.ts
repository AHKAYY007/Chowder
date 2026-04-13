import { ethers } from "hardhat";

async function main() {
  const KiteLogger = await ethers.getContractFactory("KiteLogger");
  const kiteLogger = await KiteLogger.deploy();
  await kiteLogger.waitForDeployment();

  const address = await kiteLogger.getAddress();
  console.log("KiteLogger deployed to:", address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});