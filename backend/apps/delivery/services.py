import datetime
from typing import List

from apps.delivery.models import Confirmation, Patch
from apps.projects.models import Case, Project
from common import JobStatus


def patch_exists(project_id: int, num_days: int = 1) -> bool:
    date = datetime.date.today() - datetime.timedelta(days=num_days)
    return Patch.objects.filter(project_id=project_id, date__lte=date).exists()


def check_add_patch(project: Project) -> bool:
    num_days = project.project_class.check_every_num_days
    return patch_exists(project.pk, num_days=num_days)


def get_patches() -> List[Patch]:
    patches = []
    today = datetime.date.today()
    projects = Project.objects.active().select_related("project_class")
    for _i, project in enumerate(projects):
        if not check_add_patch(project):
            patch = Patch(project=project, date=today)
            patch.save()
            patches.append(patch)
    return patches


def add_cases(patch: Patch) -> List[Confirmation]:
    project = Project.objects.prefetch_related("case_types").filter(pk=patch.project_id).first()
    case_types = project.case_types.all()
    cases = Case.objects.filter(types__in=case_types)
    if patch.status == JobStatus.SUCCESS:
        inserted_cases = Confirmation.objects.filter(patch_id=patch.id).values_list(
            "case_id", flat=True
        )
        cases = cases.exclude(pk__in=list(inserted_cases))
    confirmations = [
        Confirmation(case=case, envoy_id=case.envoy_id, patch_id=patch.id, project_id=project.id,)
        for i, case in enumerate(cases)
    ]

    return Confirmation.objects.bulk_create(confirmations, ignore_conflicts=False)


def periodically_add_patches():
    patches = get_patches()
    for _i, patch in enumerate(patches):
        add_cases(patch)
        patch.status = JobStatus.SUCCESS
        patch.save(update_fields=["status"])
