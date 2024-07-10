from mongoengine import Document, StringField, DateTimeField

# mongodbのコレクションに格納している、eventのモデル定義
class Event(Document):
    title = StringField(required=True)
    description = StringField()
    date = DateTimeField(required=True)
    location = StringField()
    meta = {
        'db_alias': 'default',
        'collection': 'events'
    }
