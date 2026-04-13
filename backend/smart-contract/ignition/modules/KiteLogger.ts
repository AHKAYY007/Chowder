import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("KiteLoggerModule", (m) => {
  const logger = m.contract("KiteLogger");

  return { logger };
});
