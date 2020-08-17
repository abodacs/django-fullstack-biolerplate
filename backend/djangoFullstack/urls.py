from django.conf.urls import include, url  # noqa
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("exampleapp/", include("exampleapp.urls"), name="exampleapp"),
]
