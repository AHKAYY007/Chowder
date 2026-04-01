from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class KiteLog(BaseModel):
    agent_id: UUID
    user_id: UUID

    action: str
    input_message: str

    decision: str
    reason: str

    amount: float

    timestamp: datetime