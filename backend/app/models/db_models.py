from sqlalchemy import Column, String, Float, Boolean, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.database import Base
from app.models.transaction import TransactionStatus


class DBUser(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now)


class DBFoodOption(Base):
    __tablename__ = "food_options"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    is_healthy = Column(Boolean, nullable=False)


class DBAgentWallet(Base):
    __tablename__ = "agent_wallets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    address = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    daily_limit = Column(Float, default=50.0)
    allowed_categories = Column(String, default="food")  # JSON or simple
    blocked_items = Column(String, default="")  # JSON


class DBTransaction(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    wallet_id = Column(UUID(as_uuid=True), ForeignKey("agent_wallets.id"))
    action = Column(String, nullable=False)
    item_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), nullable=False)
    reason = Column(String, nullable=False)
    agent_message = Column(String, nullable=False)
    tx_hash = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)


class DBKiteLog(Base):
    __tablename__ = "kite_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True))
    user_id = Column(UUID(as_uuid=True))
    action = Column(String, nullable=False)
    input_message = Column(String, nullable=False)
    decision = Column(String, nullable=False)
    reason = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)</content>
<parameter name="filePath">/home/knox/Documents/Chowder/backend/app/models/db_models.py