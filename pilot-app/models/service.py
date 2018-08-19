from mongoengine import *


# design database
class Service(Document): #Service tuong ung Collection
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField() #Kieu du lieu True/False luu thue roi hay chua thue