from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path

from rest_framework.permissions import AllowAny

from .api import api
from .views import ping


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("logout/", logout, {"next_page": "/"}, name="logout"),
    path("api/", include(api.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("ping/", ping, name="ping"),
    path("sentry-debug/", trigger_error),
]
if settings.DEBUG:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    api_info = openapi.Info(
        title="API",
        default_version="v1",
        description="api documentation",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    )
    schema_view = get_schema_view(
        info=api_info, public=True, permission_classes=(AllowAny,), patterns=urlpatterns,
    )

    urlpatterns += [
        # url(r'^__debug__/', include(debug_toolbar.urls)),
        url(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        url(
            r"^api-test/$",
            schema_view.with_ui("swagger", cache_timeout=None),
            name="schema-swagger-ui",
        ),
        url(r"^api-docs/$", schema_view.with_ui("redoc", cache_timeout=None), name="schema-redoc"),
        # url(r'^api-monitor/', include('silk.urls', namespace='silk'))
    ]
