from faker import Faker

faker = Faker()

class UserData:
    @staticmethod
    def generate_fullname() -> str:
        return faker.name()

    @staticmethod
    def generate_square(min_square=1, max_square=99999) -> int:
        return faker.random_int(min_square, max_square)

    @staticmethod
    def generate_phone_number() -> str:
        return faker.phone_number()

    @staticmethod
    def generate_email(safe=True, domain="gmail.com") -> str:
        return faker.email(safe, domain)
