from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from uuid import UUID


class UserIntent(BaseModel):
    user_id: UUID
    message: str = Field(..., description="User request")
    budget: float
    health_goal: Literal["healthy", "cheap", "anything"]
    mode: Literal["auto", "assist"] = "auto"


class AgentDecision(BaseModel):
    selected_food_id: UUID
    reason: str
    rejected_user_choice: Optional[str] = None
    confidence: float = Field(..., ge=0, le=1)


class AgentResponse(BaseModel):
    message: str
    decision: AgentDecision
    transaction_id: Optional[UUID] = None
    created_at: datetime