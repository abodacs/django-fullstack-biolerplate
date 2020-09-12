from django.template.defaultfilters import slugify

import factory
from apps.projects.models import Case
from apps.users.tests.factories import EnvoyFactory
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class CaseFactory(factory.django.DjangoModelFactory):
    famous_name = factory.Sequence(lambda n: "famous_name_%d" % (n + 1))
    code = factory.LazyAttribute(lambda a: slugify(a.famous_name))
    name = factory.Sequence(lambda n: "name_%d" % n)
    description = factory.LazyAttribute(
        lambda x: u"\n\n".join([u"{0}".format(p) for p in faker.paragraphs(nb=10)])
    )
    envoy = factory.SubFactory(EnvoyFactory)

    class Meta:
        model = Case
        django_get_or_create = [
            "code",
        ]
