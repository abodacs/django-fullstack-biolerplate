from rest_framework import routers

from .views import CaseViewSet


router = routers.DefaultRouter()
router.register("cases", CaseViewSet, "cases")

urlpatterns = router.urls
