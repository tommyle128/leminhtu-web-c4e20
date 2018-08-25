from models.service import Service
import mlab
from faker import Faker
from random import randint, choice, sample
mlab.connect()

fake = Faker()

for i in range (20):
    print("Saving service:", i+1, "....")
    profile = fake.profile()

    if profile['sex'] == 'M':
        g = 1
        h = randint(170, 185)
        desc_list = ['ga lăng', 'đam mê bóng đá', 'thích tập gym', 'học võ', 'thông minh', 'hài hước', 'menly', 'hiểu tâm lý phụ nữ']
        m_list = [randint(70, 90), randint(70, 90), randint (90, 110)]
        img_list = ['male1.jpg', 'male2.jpg', 'male3.jpg', 'male4.jpg']
    else:
        g = 0
        h = randint(155, 170)
        desc_list = ['nấu ăn ngon', 'ngoan hiền', 'dễ thương', 'chăm chỉ', 'hát hay', 'nhảy giỏi', 'lễ phép với gia đình', 'cá tính']
        m_list = [randint(80, 100), randint(60, 70), randint (80, 100)]
        img_list = ['female1.jpg', 'female2.jpg', 'female3.jpg', 'female4.jpg']

    new_service = Service(
        name = profile['name'],
        yob = randint(1990, 2000),
        gender = g, 
        height = h,
        phone = fake.phone_number(),
        address = profile['address'],
        status = choice([True, False]),
        description = sample(desc_list, 3),
        measurement = m_list,
        image = choice(img_list)
    )
    new_service.save()
    
   
     
    
  

    
