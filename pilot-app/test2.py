import mlab
from mongoengine import *
from models.service import Service
from models.user import User
from models.order import Order
import datetime

mlab.connect()

# all_users = User.objects()
# print(all_users[2].id

all_orders = Order.objects()
display_orders = []
for i in range(len(all_orders)):        
    service = Service.objects.with_id(all_orders[i]['service_id'])
    user = User.objects.with_id(all_orders[i]['user_id'])
    display = {}
    display['is_accepted'] = all_orders[i]['is_accepted']
    display['name_service'] = service['name']
    display['name_user'] = user['name']
    display['date_time']=all_orders[i]['date_time']
    display['order_id']=str(all_orders[i].id)
    display_orders.append(display)

print(display_orders)