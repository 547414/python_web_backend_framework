from datetime import datetime
from enum import Enum
from typing import Optional

from basic.model.basic_model import BasicModel


class ExampleCategoryEnum(Enum):
    DOG = "狗"
    CAT = "猫"
    FISH = "鱼"


class ExampleModel(BasicModel):
    name: str
    belong_to: str
    category: str
    desc: Optional[str] = None
    created_time: Optional[datetime] = None
