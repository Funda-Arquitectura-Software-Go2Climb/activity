from pydantic import BaseModel
from typing import Optional

class Activity(BaseModel):
    id: Optional[str]
    name: str
    description: str
    type: str
    travel: int
