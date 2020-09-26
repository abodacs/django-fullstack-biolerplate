from django.contrib import admin

from common.paginator import TimeLimitedPaginator

from .models import Confirmation, Patch
from .services import add_cases


@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    paginator = TimeLimitedPaginator
    actions = [
        "reassign_cases",
    ]
    date_hierarchy = "created_at"
    search_fields = [
        "project__title",
    ]
    list_display = (
        "project",
        "date",
    )
    list_select_related = ("project",)
    raw_id_fields = ["project"]

    def reassign_cases(self, request, queryset):
        for _i, patch in enumerate(queryset):
            add_cases(patch)

    reassign_cases.short_description = "Reassign cases"


@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    paginator = TimeLimitedPaginator
    show_full_result_count = False
    date_hierarchy = "created_at"
    list_display = (
        "project",
        "case",
        "envoy",
        "patch",
        "delivered",
    )
    list_select_related = (
        "project",
        "case",
        "envoy",
        "patch",
    )
    list_filter = [
        "delivered",
    ]

    raw_id_fields = [
        "project",
        "case",
        "envoy",
        "patch",
    ]
