from mongoengine import *

# Design database:
class Video(Document):
    title = StringField()
    views = IntField()
    thumbnail = StringField()
    youtube_id = StringField()
    link = StringField()

        
