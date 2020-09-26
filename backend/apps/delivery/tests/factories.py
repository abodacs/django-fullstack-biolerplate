import factory
from apps.delivery.models import Confirmation, Patch
from apps.projects.tests.factories import CaseFactory, EnvoyFactory, ProjectFactory
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class PatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patch
        django_get_or_create = ["project", "date"]

    project = factory.SubFactory(ProjectFactory)
    date = faker.date_time_between(start_date="+1d", end_date="+45d")
    closed = False


class ConfirmationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Confirmation
        django_get_or_create = ["patch", "project", "case", "envoy"]

    project = factory.SubFactory(ProjectFactory)
    patch = factory.SubFactory(PatchFactory, project=factory.SelfAttribute("..project"))
    envoy = factory.SubFactory(EnvoyFactory)
    case = factory.SubFactory(CaseFactory, envoy=factory.SelfAttribute("..envoy"))
    delivered = None
