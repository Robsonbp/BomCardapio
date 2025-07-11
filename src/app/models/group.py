# Bibiotecas Padrões
import uuid
from datetime import datetime, timezone

# Bibliotecas de Terceiros
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

# Imports locais
from app.db.session import Base


class Group(Base):
    __tablename__ = "GROUPS"

    id = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False
    )

    name = Column(String(length=100),nullable=False)

    owner_id = Column(
        PG_UUID(as_uuid=True),
        ForeignKey("USERS.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint("owner_id", "name", name="uq_group_owner_name"),
    )

    owner = relationship("User", back_populates="groups")
