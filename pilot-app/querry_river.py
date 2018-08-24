import mlab
from models.river import River

mlab.connect2()

print('All rivers in Africa:')
africa_rivers = River.objects(continent='Africa')
for i in range (len(africa_rivers)):
    print(africa_rivers[i]['name'])

print('All rivers in South America having length that is less than 1000 kilometers:')
american_rivers = River.objects(continent='S. America', length__lt=1000)
for j in range (len(american_rivers)):
    print(american_rivers[j]['name'])


