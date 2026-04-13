# KiteLogger Contract - Hardhat

Build & Deploy a KiteLogger Contract on Kite AI using Hardhat

This project follows the [Kite AI Hardhat Counter Tutorial](https://docs.gokite.ai/kite-chain/4-building-dapps/counter-contract-hardhat) but implements a `KiteLogger` contract for autonomous AI decision logging instead of a simple counter.

## Setup

1. Install dependencies: `pnpm install`
2. Copy `.env.example` to `.env` and fill in your values
3. Compile: `pnpm exec hardhat compile`
4. Test: `pnpm exec hardhat test`

## Deployment

### Using Ignition (Recommended for Hardhat 3)
```bash
pnpm exec hardhat ignition deploy --network kiteTestnet ignition/modules/KiteLogger.ts
```

### Using Script (Alternative)
```bash
pnpm exec hardhat run scripts/deploy.ts --network kiteTestnet
```

## Environment Variables

See `.env.example` for required variables:
- `PRIVATE_KEY`: Your wallet private key
- `KITE_RPC_URL`: Kite testnet RPC URL
- `KITE_CHAIN_ID`: Chain ID (2367 for testnet)
- `KITE_EXPLORER_BROWSER_URL`: Explorer URL

## Contract Features

- Owner-controlled agent authorization
- On-chain logging of AI decisions
- Event emission for transparency
- User log retrieval
