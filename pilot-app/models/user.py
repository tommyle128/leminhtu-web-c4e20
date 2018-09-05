from mongoengine import *

class User(Document):
    name = StringField()
    email = EmailField()
    username = StringField()
    password = StringField()
