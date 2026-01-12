from database import Base

from sqlalchemy import Column, Integer, String, DateTime, func


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    # timezone=True допускает поправку на временную зону
    # server_default=func.now() устанавливает текущее время автоматически
    created_at = Column(DateTime(timezone=True), server_default=func.now())