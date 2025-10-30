from faker import Faker

fake  = Faker('ru_RU')
print(fake.name())
print(fake.address())
print(fake.email())


date = {
    "email": fake.email(),
    "name": fake.name(),
    "age": fake.random_int(18, 30)
}


print(date)