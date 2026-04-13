from langchain.tools import tool
from app.models.food import FoodOption, FoodQuery
from app.models.transaction import Transaction, TransactionStatus
from app.models.kite import KiteLog
from app.models.wallet import AgentWallet
from uuid import uuid4
from datetime import datetime
import random
from web3 import Web3
from app.core.config import settings

# Contract ABI (placeholder - replace with actual after deployment)
KITE_LOGGER_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "agent", "type": "address"}
        ],
        "name": "authorizeAgent",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "user", "type": "address"},
            {"internalType": "string", "name": "action", "type": "string"},
            {"internalType": "string", "name": "inputMessage", "type": "string"},
            {"internalType": "string", "name": "decision", "type": "string"},
            {"internalType": "string", "name": "reason", "type": "string"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "logAction",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Contract address is configured via environment and should point to the deployed KiteLogger contract
CONTRACT_ADDRESS = settings.kite_logger_address

w3 = Web3(Web3.HTTPProvider(settings.kite_rpc_url))
contract = None
account = None
if CONTRACT_ADDRESS:
    try:
        contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=KITE_LOGGER_ABI)
    except Exception:
        contract = None

if settings.kite_private_key:
    account = w3.eth.account.from_key(settings.kite_private_key)


@tool
async def fetch_food(max_price: float, prefer_healthy: bool = False) -> list[FoodOption]:
    """Fetch food options from the menu based on budget and health preference."""
    # Mock food options for MVP
    foods = [
        FoodOption(id=uuid4(), name="Burger", price=8.99, calories=500, is_healthy=False),
        FoodOption(id=uuid4(), name="Salad", price=6.99, calories=200, is_healthy=True),
        FoodOption(id=uuid4(), name="Pizza Slice", price=4.99, calories=300, is_healthy=False),
        FoodOption(id=uuid4(), name="Smoothie", price=5.99, calories=150, is_healthy=True),
        FoodOption(id=uuid4(), name="Fries", price=3.99, calories=400, is_healthy=False),
    ]
    
    # Filter by price and preference
    filtered = [f for f in foods if f.price <= max_price]
    if prefer_healthy:
        filtered = [f for f in filtered if f.is_healthy]
    
    return filtered if filtered else foods  # Return all if none match


@tool
async def make_payment(food_id: str, amount: float, wallet_id: str) -> Transaction:
    """Make a payment for the selected food using the agent wallet."""
    # Mock payment logic
    # In real impl, check wallet balance, deduct, etc.
    # For now, assume success
    tx = Transaction(
        id=uuid4(),
        user_id=uuid4(),  # Mock user
        wallet_id=uuid4(),  # Mock wallet
        action="food_order",
        item_name="Selected Food",  # Would map from food_id
        amount=amount,
        status=TransactionStatus.SUCCESS,
        reason="Autonomous decision",
        agent_message="Paid for your meal, you lazy bum.",
        tx_hash=f"mock_tx_{random.randint(1000,9999)}",  # Mock hash
        created_at=datetime.now()
    )
    return tx


@tool
async def log_action(agent_id: str, user_id: str, action: str, input_message: str, decision: str, reason: str, amount: float) -> str:
    """Log the action on-chain via Kite."""
    # For now, mock - replace with actual contract call after deployment
    # tx = contract.functions.logAction(user_id, action, input_message, decision, reason, int(amount)).transact()
    # receipt = w3.eth.wait_for_transaction_receipt(tx)
    # return receipt.transactionHash.hex()
    if contract and account:
        nonce = w3.eth.get_transaction_count(account.address)
        tx = contract.functions.logAction(
            user_id,
            action,
            input_message,
            decision,
            reason,
            int(amount),
        ).build_transaction({
            "from": account.address,
            "nonce": nonce,
            "gas": 500000,
            "gasPrice": w3.eth.gas_price,
            "chainId": settings.kite_chain_id,
        })
        signed = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction).hex()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_hash

    tx_hash = f"kite_tx_{random.randint(10000,99999)}"
    return tx_hash