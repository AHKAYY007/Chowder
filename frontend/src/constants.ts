import { ethers } from "ethers";

export const KITE_LOGGER_ADDRESS = "0xYourContractAddressHere"; // Replace with actual deployed address

export const KITE_LOGGER_ABI = [
  "function authorizeAgent(address agent) public",
  "function logAction(string memory action, uint256 value) public",
];
