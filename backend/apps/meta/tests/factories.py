import random

from django.template.defaultfilters import slugify

import factory
from apps.meta.models import Area, CaseType, Problem, ProjectClass
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class ProjectClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectClass
        django_get_or_create = ("slug",)

    name = factory.Sequence(lambda n: "Project class %d" % (n + 1))
    slug = factory.LazyAttribute(lambda a: slugify(a.name))
    type = factory.LazyAttribute(lambda x: random.choice(ProjectClass.TYPE_CHOICES))


class ProblemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Problem
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: "Problem %d" % (n + 1))
    order = factory.Sequence(lambda n: (n + 1))


class CaseTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CaseType
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: "Case Type %d" % (n + 1))
    order = factory.Sequence(lambda n: (n + 1))


class AreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Area
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: "Area %d" % (n + 1))
    order = factory.Sequence(lambda n: (n + 1))
