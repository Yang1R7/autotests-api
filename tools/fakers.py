import time
from faker import Faker



class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email(domain="max.com")

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def lastname(self) -> str:
        return self.faker.last_name()

    def firstname(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def estimated_time(self) -> str:
        return f"{self.integer(1, 10)} weeks"

    def integer(self, star: int = 1, end: int = 100):
        return self.faker.random_int(star, end)

    def max_score(self) -> int:
        return self.integer(50, 100)

    def min_score(self) -> int:
        return self.integer(1, 30)




fake = Fake(faker=Faker())