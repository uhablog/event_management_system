import strawberry
from strawberry.types import Info
from datetime import datetime
from fastapi import Depends
from typing import List, Optional

# from schemas.types import EventType
from ..schemas.types import EventType
# from app.schemas.types import EventType

@strawberry.type
class Query:
    @strawberry.field
    def events(self, info: Info) -> List[EventType]:
      service = info.context.get("event_service")
      return service.get_all_events()

    @strawberry.field
    def event_by_id(self, event_id: strawberry.ID, info: Info) -> EventType:
        service = info.context.get("event_service")
        return service.get_event_by_id(str(event_id))

    # @strawberry.field
    # def search_events(self, keyword: Optional[str] = None, date: Optional[datetime] = None) -> List[EventType]:
    #     query = {}
    #     if keyword:
    #         query['$text'] = {'$search': keyword}
    #     if date:
    #         query['date'] = date
    #     return [EventType.from_mongo(event) for event in Event.objects(__raw__=query)]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_event(
        self,
        title: str,
        description: Optional[str],
        date: datetime,
        location: Optional[str],
        info: Info
    ) -> EventType:
        service = info.context.get("event_service")
        return service.create_event(title=title, description=description, date=date, location=location)

    # @strawberry.mutation
    # def update_event(self, id: strawberry.ID, title: Optional[str] = None, description: Optional[str] = None, date: Optional[datetime] = None, location: Optional[str] = None) -> EventType:
    #     event = Event.objects(id=id).first()
    #     if not event:
    #         raise Exception("Event not found")
    #     event.update(title=title, description=description, date=date, location=location)
    #     return EventType.from_mongo(event.reload())

    @strawberry.mutation
    def delete_event(
        self,
        id: strawberry.ID,
        info: Info
    ) -> EventType:
        service = info.context.get("event_service")
        deleted = service.delete_event(str(id))
        if not deleted:
            raise Exception("Event not found")
        return EventType(id=id)

schema = strawberry.Schema(query=Query, mutation=Mutation)