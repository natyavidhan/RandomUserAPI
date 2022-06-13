from faker import Faker
import json


faker = Faker()

def generate_profile(seed=None):
    if seed:
        Faker.seed(seed)
    return faker.profile()