import mlab
from models.service import Service

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[4]

# print(first_service['name'])

id_to_find = '5b781ef869151b0f10ea8bda'

# hera = Service.objects(id=id_to_find) ## => trả ra list: []
# hera2 = Service.objects.get(id=id_to_find) ## => Service obj
service = Service.objects.with_id(id_to_find) ## => Service obj

if service is not None:
    # service.delete()
    # print("Deleted")
    print("Before: ")
    print(service.to_mongo())
    service.update(set__yob=2005, set__name='Link Kute')
    service.reload()
    print("After: ")
    print(service.to_mongo())
else:
    print("Not found")