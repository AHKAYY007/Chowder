import { expect } from "chai";
import { network } from "hardhat";

const { ethers } = await network.connect();

describe("KiteLogger", function () {
  it("should allow the owner to authorize agents and create logs", async function () {
    const logger = (await ethers.deployContract("KiteLogger")) as any;
    const [owner, agentSigner, userSigner] = await ethers.getSigners();
    const user = await userSigner.getAddress();

    await expect(logger.authorizeAgent(agentSigner.address)).to.emit(logger, "AgentAuthorized").withArgs(agentSigner.address);
    await expect(
      logger.connect(agentSigner).logAction(
        user,
        "food_order",
        "Order healthy lunch",
        "Selected salad",
        "Staying under budget and healthy",
        12n,
      ),
    ).to.emit(logger, "LogCreated");

    const ids = await logger.getUserLogIds(user);
    expect(ids.length).to.equal(1);

    const log = await logger.logs(ids[0]);
    expect(log.agent).to.equal(agentSigner.address);
    expect(log.user).to.equal(user);
    expect(log.action).to.equal("food_order");
    expect(log.amount).to.equal(12n);
  });

  it("should reject logAction from unauthorized agents", async function () {
    const logger = (await ethers.deployContract("KiteLogger")) as any;
    const [, unauthorizedSigner, userSigner] = await ethers.getSigners();
    const user = await userSigner.getAddress();

    await expect(
      logger.connect(unauthorizedSigner).logAction(
        user,
        "food_order",
        "Order pizza",
        "Selected pizza",
        "Cheaper than salad",
        10n,
      ),
    ).to.be.revertedWith("KiteLogger: caller is not authorized");
  });
});
