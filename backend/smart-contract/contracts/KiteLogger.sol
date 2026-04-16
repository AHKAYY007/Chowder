// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

contract KiteLogger {
    address public owner;
    uint256 public nextLogId = 1;

    struct LogEntry {
        address agent;
        address user;
        string action;
        string inputMessage;
        string decision;
        string reason;
        uint256 amount;
        uint256 timestamp;
    }

    mapping(uint256 => LogEntry) public logs;
    mapping(address => bool) public authorizedAgents;
    mapping(address => uint256[]) private userLogIds;

    event AgentAuthorized(address indexed agent);
    event AgentRevoked(address indexed agent);
    event LogCreated(uint256 indexed logId, address indexed agent, address indexed user, string action, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "KiteLogger: caller is not owner");
        _;
    }

    modifier onlyAuthorizedAgent() {
        require(authorizedAgents[msg.sender], "KiteLogger: caller is not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
        authorizedAgents[msg.sender] = true;
    }

    function authorizeAgent(address agent) external onlyOwner {
        require(agent != address(0), "KiteLogger: invalid agent");
        authorizedAgents[agent] = true;
        emit AgentAuthorized(agent);
    }

    function revokeAgent(address agent) external onlyOwner {
        require(agent != address(0), "KiteLogger: invalid agent");
        authorizedAgents[agent] = false;
        emit AgentRevoked(agent);
    }

    function logAction(
        address user,
        string calldata action,
        string calldata inputMessage,
        string calldata decision,
        string calldata reason,
        uint256 amount
    ) external onlyAuthorizedAgent returns (uint256) {
        require(user != address(0), "KiteLogger: invalid user");
        require(bytes(action).length > 0, "KiteLogger: action required");
        require(bytes(decision).length > 0, "KiteLogger: decision required");
        require(amount > 0, "KiteLogger: amount must be positive");

        uint256 logId = nextLogId++;
        logs[logId] = LogEntry({
            agent: msg.sender,
            user: user,
            action: action,
            inputMessage: inputMessage,
            decision: decision,
            reason: reason,
            amount: amount,
            timestamp: block.timestamp
        });
        userLogIds[user].push(logId);

        emit LogCreated(logId, msg.sender, user, action, amount);
        return logId;
    }

    function getUserLogIds(address user) external view returns (uint256[] memory) {
        return userLogIds[user];
    }
}
