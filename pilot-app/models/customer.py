from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()



