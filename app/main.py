from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schemas.graphql import schema
from dependencies import get_db, get_context

# GraphQLのエンドポイントを設定する
graphql_app = GraphQLRouter(
    schema
    , context_getter=get_context
    # , graphiql=True
)
# graphql_app = GraphQLRouter(schema)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # アプリケーションが起動する時にデータベース接続を初期化
    print('データベースの接続')
    get_db()

# GraphQLのルートをアプリケーションに追加
app.include_router(graphql_app, prefix="/graphql")