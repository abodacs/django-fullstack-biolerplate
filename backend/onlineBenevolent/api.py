from apps.delivery.views import ConfirmationViewSet, PatchViewSet
from apps.projects.views import CaseViewSet
from apps.users.views import UserViewSet
from rest_framework import routers


# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

# Users API
api.register(r"users", UserViewSet)

# Case API
api.register("cases", CaseViewSet, "cases")

# Patch API
api.register("patches", PatchViewSet, "patches")

# Confirmation API
api.register("confirmations", ConfirmationViewSet, "confirmations")
