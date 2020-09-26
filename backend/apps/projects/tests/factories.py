from django.template.defaultfilters import slugify

import factory
from apps.meta.tests.factories import ProjectClassFactory
from apps.projects.models import Case, Project
from apps.users.tests.factories import EnvoyFactory
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class CaseFactory(factory.django.DjangoModelFactory):
    famous_name = factory.Sequence(lambda n: "famous_name_%d" % (n + 1))
    code = factory.LazyAttribute(lambda a: slugify(a.famous_name))
    name = factory.Sequence(lambda n: "name_%d" % n)
    description = factory.LazyAttribute(
        lambda x: "\n\n".join(["{0}".format(p) for p in faker.paragraphs(nb=10)])
    )
    envoy = factory.SubFactory(EnvoyFactory)

    class Meta:
        model = Case
        django_get_or_create = [
            "code",
        ]


class ProjectFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: "title_%d" % n)
    description = factory.LazyAttribute(
        lambda x: "\n\n".join(["{0}".format(p) for p in faker.paragraphs(nb=10)])
    )
    project_class = factory.SubFactory(ProjectClassFactory, name="day")
    start_date = faker.date_time_between(start_date="+1d", end_date="+45d")

    class Meta:
        model = Project
        django_get_or_create = [
            "title",
        ]

    @factory.post_generation
    def envoys(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            envoys_model = Project.envoys.through
            # print('extracted:::extracted', extracted)
            project_envoys = [envoys_model(user=envoy, project=self) for envoy in extracted]
            envoys_model.objects.bulk_create(project_envoys, ignore_conflicts=True)

    @factory.post_generation
    def case_types(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            case_types_model = Project.case_types.through
            project_case_types = (
                case_types_model(case_type=case_type, project=self) for case_type in extracted
            )
            case_types_model.objects.bulk_create(project_case_types, ignore_conflicts=True)
