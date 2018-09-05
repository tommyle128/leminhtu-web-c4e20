from mongoengine import *

class Order(Document):
    service_id = StringField()
    user_id = StringField()
    is_accepted = BooleanField()
    date_time = DateTimeField()