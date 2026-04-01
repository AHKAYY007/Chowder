from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime
from uuid import UUID
from enum import Enum


class TransactionStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"


class Transaction(BaseModel):
    id: UUID
    user_id: UUID
    wallet_id: UUID

    action: Literal["food_order", "api_payment"]

    item_name: str
    amount: float = Field(..., gt=0)

    status: TransactionStatus

    reason: str  # WHY agent did it
    agent_message: str  # personality output

    tx_hash: Optional[str] = None  # Kite hash

    created_at: datetime