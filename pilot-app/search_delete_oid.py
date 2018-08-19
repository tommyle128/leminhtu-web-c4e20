import mlab
from mongoengine import *
from models.service import Service

mlab.connect()

id_to_find = "5b7825e769151b0eb023698b"
doc_id = Service.objects.get(id=id_to_find)
doc_id.delete()
