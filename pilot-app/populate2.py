from models.customer import Customer
import mlab
from faker import Faker
from random import choice

mlab.connect()

fake = Faker()
for i in range (50):
    print("Saving to Customer (Collection)",i+1,"...")

    profile = fake.profile()
    if profile['sex'] == 'M':
        g = 1
    else:
        g = 0

    new_customer = Customer(
        name =  profile['name'],
        gender = g,
        email = profile['mail'],
        phone = fake.phone_number(),
        job = profile['job'],
        company = profile['company'],
        contacted = choice([True, False])
    )
    new_customer.save()



