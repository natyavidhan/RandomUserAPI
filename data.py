from faker import Faker
import json
import random

faker = Faker()

def generate_profile(seed=None, amount=1):
    seed = seed or random.randint(0, 1000000)
    Faker.seed(seed)
    ret = []
    for i in range(int(amount)):
        profile = faker.profile()
        profile['phone'] = faker.phone_number()
        profile['picture'] = "https://derpy-peeps.vercel.app/image?seed=" + str(seed)
        ret.append(profile)
    return ret

def get_root():
    return faker