from datetime import datetime
from typing import List, Optional

# from schemas.types import EventType
# from models.event import Event
from ..schemas.types import EventType
from ..models.event import Event
# from app.schemas.types import EventType
# from app.models.event import Event

class EventService:
    def create_event(
        self,
        title: str,
        description: Optional[str],
        date: datetime,
        location: Optional[str]
    ) -> Event:
        """
        新しいイベントを作成する。
        """
        event = Event(
            title=title,
            description=description,
            date=date,
            location=location
        )
        event.save()
        event = self.convert_to_event_type(event)
        return event

    def get_all_events(self) -> List[EventType]:
        """
        すべてのイベントを取得する。
        """
        events = list(Event.objects)
        return [self.convert_to_event_type(event) for event in events]

    def get_event_by_id(self, event_id: str) -> Optional[EventType]:
        """
        特定のIDを持つイベントを取得する。
        """
        event = Event.objects(id=event_id).first()
        return self.convert_to_event_type(event)

    def update_event(
        self,
        event_id: str,
        title: Optional[str],
        description: Optional[str],
        date: Optional[datetime],
        location: Optional[str]
    ) -> Optional[Event]:
        """
        指定されたIDのイベントを更新する。
        """
        event = Event.objects(id=event_id).first()
        if not event:
            return None
        
        event.update(
            title=title if title is not None else event.title,
            description=description if description is not None else event.description,
            date=date if date is not None else event.date,
            location=location if location is not None else event.location
        )
        return event.reload()

    def delete_event(self, event_id: str) -> bool:
        """
        指定されたIDのイベントを削除する。
        """
        event = Event.objects(id=event_id).first()
        if not event:
            return False
        
        event.delete()
        return True
    
    def convert_to_event_type(self, event: Event) -> EventType:
        return EventType(
            id=str(event.id),
            title=event.title,
            description=event.description,
            date=event.date,
            location=event.location
        )
