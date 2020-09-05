from faker import Faker
from faker.providers import BaseProvider


fake = Faker("ar_EG")


class MobileNumberProvider(BaseProvider):
    mobile_formats = ("+02##########",)

    def mobile_number(self):
        return self.numerify(self.random_element(self.mobile_formats))


fake.add_provider(MobileNumberProvider)
