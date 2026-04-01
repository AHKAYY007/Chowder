from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID


class SpendingConstraints(BaseModel):
    daily_limit: float = Field(..., gt=0)
    allowed_categories: List[str] = ["food"]
    blocked_items: List[str] = []


class AgentWallet(BaseModel):
    wallet_id: UUID
    user_id: UUID
    address: str
    balance: float
    constraints: SpendingConstraints


class FundWalletRequest(BaseModel):
    user_id: UUID
    amount: float = Field(..., gt=0)