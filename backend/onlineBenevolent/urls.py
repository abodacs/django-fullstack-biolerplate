from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import path

from .views import ping


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("ping/", ping, name="ping"),
    path("sentry-debug/", trigger_error),
]
