from django.contrib import admin

from .models import Area, CaseType, Problem, ProjectClass


@admin.register(ProjectClass)
class ProjectClassAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
    )


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )


@admin.register(CaseType)
class CaseTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )
