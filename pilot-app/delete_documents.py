import mlab
import mongoengine
from models.service import Service

mlab.connect()

all_docs = Service.objects

for index, value in enumerate (Service.objects):
    all_docs[index].delete()
    print("Deleted item: ", index)

