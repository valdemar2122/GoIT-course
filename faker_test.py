from faker import Faker, Factory
import json
fake = Factory.create("uk_UA")

users = []

def create_users(fake, users: list, n=10):
    for _ in range(n):
        user = {}
        user["name"] = fake.name()
        user["phone_number"] = fake.phone_number()
        user["email"] = fake.email()
        user["address"] = fake.address()
        user["birthday"] = fake.date()
        users.append(user)


def to_file(users):
    with open ("users.json", 'w') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)
        


if __name__ == "__main__":
    create_users(fake, users, 12)
    to_file(users)