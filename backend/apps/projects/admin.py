from django.contrib import admin

from .models import Case, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project_class",
    )

    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        qs = qs.select_related("project_class",)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_filter = ("envoy",)
    list_display = (
        "name",
        "envoy",
    )

    def get_queryset(self, request):
        qs = super(CaseAdmin, self).get_queryset(request)
        qs = qs.select_related("envoy",)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
