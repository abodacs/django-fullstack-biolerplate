from django.contrib import admin

from .models import Place, Problem, ProjectClass


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


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )
