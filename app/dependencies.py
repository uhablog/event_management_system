import os
from mongoengine import connect

from services.event_service import EventService

# mongodbへの接続を取得する
def get_db():
    username = os.getenv('MONGO_USER')
    password = os.getenv('MONGO_PASS')
    host = os.getenv('MONGO_HOST')
    port = os.getenv('MONGO_PORT')
    dbname = os.getenv('MONGO_DB')
    print('get_dbするよ');
    print(f"mongodb://{username}:{password}@{host}:{port}/{dbname}")
    db = connect(
        db=dbname,
        host=f"mongodb://{username}:{password}@{host}:{port}/{dbname}?authSource=admin",
        alias="default",
        maxPoolSize=200,
        waitQueueTimeoutMS=3000
    )
    # db = connect(
    #     db="myeventdb",
    #     host="mongodb://mongo:mongo@mongodb:27017/myeventdb",
    #     alias="default",
    #     maxPoolSize=200,  # プールサイズを200に設定
    #     waitQueueTimeoutMS=3000  # 接続待ちの最大時間（ミリ秒）
    # )
    return db

async def get_context():
    return {
        "event_service": get_event_service()
    }

# EventServiceクラスのインスタンスを取得する
def get_event_service():
    return EventService()