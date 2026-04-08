# 🍔🤖 Chowder — Autonomous AI Food Agent

## 🚀 Overview

**Chowder** is an autonomous AI agent with wallet capabilities that **decides what you eat, executes payments, and proves every action on-chain**.

It is not a recommendation system.

> Chowder does not suggest — it **decides, pays, and logs**.

Built for the **Agent-Native Infrastructure paradigm**, Chowder combines:
- AI reasoning
- Economic execution
- On-chain accountability

---

## ⚡ Core Idea

Users don’t micromanage choices.

They define constraints like:
- “Eat healthy”
- “Stay under $12”
- “Avoid junk”

Chowder:
1. Finds options
2. Makes the decision
3. Executes payment
4. Logs it on-chain

---

## 🧠 Key Capabilities

### 🤖 Autonomous Decision Engine
- Interprets user intent
- Selects optimal food without approval
- Uses structured reasoning (Pydantic-AI)

---

### 💸 Agent Wallet Execution
- AI-controlled wallet (Account Abstraction)
- Executes payments (USDC/test tokens)
- Supports gasless transactions (Kite SDK)

---

### 🛡️ Constraint Enforcement
- Budget limits
- Health filters
- Custom rules:
  - “No junk food”
  - “Max daily spend”
  - “Avoid allergens”

---

### 🧾 Transaction History (Trust Layer)
- Logs:
  - item purchased
  - amount spent
  - reasoning
  - timestamp
- Enables transparency + accountability

---

### ⛓️ On-Chain Logging (Kite)
- All decisions recorded on-chain
- Verifiable and tamper-proof
- Supports attestations for auditability

---

### 🌐 External API Awareness
- Can integrate with:
  - Uber Eats / food APIs
  - Nutrition APIs
- Makes real-world informed decisions

---

### ⚠️ Safety Awareness
- Tracks user allergies
- Avoids harmful food selections
- Prevents risky or invalid transactions

---

## 💼 Wallet Features (User-Facing)

### ✅ MVP Wallet Features
- Agent wallet (auto-created)
- Balance display
- Transaction history
- Spending constraints

---

### 🔄 Funding Options
- Connect wallet (e.g. MetaMask)
- Transfer funds to agent wallet
- Optional: direct funding via UI

---

### 🎯 Smart Thresholds (Core Intelligence)

Users can define rules like:
- Daily food budget
- Junk food limits
- Spending categories (food, data, etc.)
- Health goals

Chowder enforces them automatically.

---

## 🧱 Architecture

### 🔁 Flow

1. User sends intent (chat UI)
2. Agent processes input
3. Fetches food options (API/tool)
4. Generates structured decision (Pydantic-AI)
5. Executes payment (wallet tool)
6. Logs action on Kite
7. Returns response + transaction

---

## 🧠 AI Stack

### 🧩 Pydantic-AI
- Enforces structured outputs
- Ensures:
  - valid decisions
  - consistent schemas
  - safe execution

---

### 🔗 LangChain
- Orchestrates agent workflow
- Handles:
  - tool calling
  - reasoning steps
  - execution flow

---

## 🛠️ Kite SDK Integration

Chowder integrates with Kite ecosystem:

### 🔐 Account Abstraction (AA SDK)
- Creates agent wallets
- Enables programmable spending
- Allows autonomous transactions

---

### ⚡ Gasless Transactions
- Improves UX (no gas friction)
- Ideal for autonomous agents

---

### 🪪 Agent Passport Demo
- Provides identity layer for agents
- Enables:
  - agent verification
  - trust layer for execution
- Chowder uses this to:
  - register agent identity
  - associate actions with a verifiable agent

---

### 📊 Indexer
- Fetch on-chain transaction history
- Sync UI with blockchain state

---

### ⛓️ Attestations / Logging
- Records:
  - decisions
  - payments
  - reasoning
- Ensures auditability

---

## 🖥️ Interface

### 💬 Chat-Based UI
- Primary interaction layer
- Users give intent, not commands

---

### 📊 Dashboard
- Wallet balance
- Transaction history
- Agent decisions
- Constraint settings

---

## 🎭 Example Scenarios

### 🥗 Healthy Mode
**User:**  
“Eat healthy under $12”

**Chowder:**  
“I blocked shawarma. Picked grilled chicken salad. Paid. Stay focused.”

---

### 💸 Budget Mode
**User:**  
“I’m broke”

**Chowder:**  
“You’ve got $6 and bad habits. I picked rice and beans. Payment done.”

---

### 🚫 Bad Decision Prevention
**User:**  
“Order shawarma”

**Chowder:**  
“No. We’ve learned nothing, clearly. I fixed it.”

---

### 🤖 Autonomous Mode
(No user input)

**Chowder:**  
“You haven’t eaten properly. I handled it.”

---

## 🎯 MVP Scope (Hackathon Focus)

### ✅ Build Now
- Chat interface
- Agent decision + execution
- Mock food API
- Wallet simulation / AA integration
- Transaction history (SQLite)
- Kite logging

---

### 🚀 Add Later (Extensions)

- Real food APIs (Uber Eats)
- Cross-chain payments
- Subscription meal plans
- Multi-agent coordination
- Health tracking integrations
- Advanced financial planning (data, insurance, etc.)

---

## 🏁 Goal

Build a **fully autonomous AI agent** that:
- Makes real decisions
- Executes economic actions
- Enforces rules
- Logs everything on-chain

---

## 🔥 One-Liner

**Chowder is an autonomous AI agent that decides what you eat, pays for it, and proves it on-chain — without asking you twice.**