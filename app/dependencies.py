import os
from mongoengine import connect

# from services.event_service import EventService
from .services.event_service import EventService
# from app.services.event_service import EventService

# mongodbへの接続を取得する
def get_db():
    username = os.getenv('MONGO_USER')
    password = os.getenv('MONGO_PASS')
    host = os.getenv('MONGO_HOST')
    port = os.getenv('MONGO_PORT')
    dbname = os.getenv('MONGO_DB')
    db = connect(
        db=dbname,
        host=f"mongodb://{username}:{password}@{host}:{port}/{dbname}?authSource=admin",
        alias="default",
        maxPoolSize=200,
        waitQueueTimeoutMS=3000
    )
    return db

async def get_context():
    return {
        "event_service": get_event_service()
    }

# EventServiceクラスのインスタンスを取得する
def get_event_service():
    return EventService()