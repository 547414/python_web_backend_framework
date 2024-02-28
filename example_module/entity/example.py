from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, func

from basic import BaseEntity


class ExampleEntity(BaseEntity):
    __tablename__ = 'ct_example'

    id = Column(String(255), primary_key=True, default=func.uuid_generate_v4())
    name = Column(String(255), nullable=False)
    belong_to = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    desc = Column(Text, nullable=True)
    created_time = Column(DateTime(timezone=True), default=datetime.now)
