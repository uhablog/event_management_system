import strawberry
from datetime import datetime
from typing import Optional

@strawberry.type
class EventType:
    id: strawberry.ID
    title: str
    description: Optional[str]
    date: datetime
    location: Optional[str]