from django.contrib.auth import get_user_model

import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("username")
    name = factory.Faker("name")
    password = "test"

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class EnvoyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.Envoy"
        django_get_or_create = ["username"]

    username = factory.Faker("username")
    name = factory.Faker("name")
