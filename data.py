from faker import Faker
import json


faker = Faker()

def generate_profile(seed=None, amount=1):
    if seed:
        Faker.seed(seed)
    ret = []
    for i in range(int(amount)):
        profile = faker.profile()
        profile['phone'] = faker.phone_number()
        ret.append(profile)
    return ret

def get_root():
    return faker