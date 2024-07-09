from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from mongoengine import connect

# MongoDBへの接続
connect(db="myeventdb", host="mongodb://mongo:mongo@mongodb:27017/myeventdb", alias="default")

@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello {name}"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()

# GraphQLのエンドポイントを追加
app.include_router(graphql_app, prefix="/graphql")
