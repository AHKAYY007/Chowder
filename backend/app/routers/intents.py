from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.agent import UserIntent, AgentResponse, AgentDecision
from app.agent.chowder_agent import run_agent
from app.core.logger import logger
from uuid import uuid4
from datetime import datetime


router = APIRouter(prefix="/intents", tags=["intents"])


@router.post("/", response_model=AgentResponse)
async def submit_intent(intent: UserIntent, db: AsyncSession = Depends(get_db)):
    logger.info(f"Received intent: {intent.message}")
    
    # Run the agent
    input_text = f"User intent: {intent.message}, Budget: {intent.budget}, Health goal: {intent.health_goal}"
    result = run_agent(input_text)
    
    # Parse result to AgentResponse
    # For now, mock
    decision = AgentDecision(
        selected_food_id=uuid4(),
        reason=result.get("output", "Agent decided"),
        confidence=0.9
    )
    response = AgentResponse(
        message=result.get("output", "Done"),
        decision=decision,
        transaction_id=uuid4(),
        created_at=datetime.now()
    )
    
    return response