from models.service import Service
import mlab
from faker import Faker
from random import randint, choice, sample
mlab.connect()

fake = Faker()
for i in range (10):
    print("Saving service", i+1, "....")
    
    profile = fake.profile()
    
     if profile['sex'] == 'M':
        g = 1
        h_list = randint(170, 190)
        des_list = ['ga lăng', 'đam mê bóng đá', 'thích tập gym', 'học võ', 'thông minh', 'hài hước', 'menly', 'hiểu tâm lý phụ nữ']
        m_list = [randint(70, 90), randint(70, 90), randint (80, 100)]
        img

    else:
        g = 0
        h_list = randint(155, 170)
        des_list = ['nấu ăn ngon', 'ngoan hiền', 'dễ thương', 'chăm chỉ', 'hát hay', 'nhảy giỏi', 'lễ phép với gia đình', 'cá tính']
        img_link = 
    

    new_service = Service(
        name = profile['name'],
        yob=randint(1990, 2000),
        gender=g, 
        height=h_list,
        phone=fake.phone_number(),
        address=profile['address'],
        status=choice([True, False]),
        description=sample(des_list, 4)
        measurement=m_list
        image=choice(img_link)
    )
    new_service.save()
