from faker import Faker
import json


faker = Faker()

def generate_profile(seed=None):
    if seed:
        Faker.seed(seed)
    profile = faker.profile()
    profile['phone'] = faker.phone_number()
    return profile

def get_root():
    return faker