from faker import Faker

fake = Faker("ru_RU")
name = fake.first_name_female()

print(fake.first_name_female())
print(fake.last_name_female())
print(fake.street_name())
print(fake.phone_number())