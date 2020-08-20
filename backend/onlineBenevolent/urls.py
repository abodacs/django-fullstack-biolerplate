from django.conf.urls import include, url  # noqa
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
]
