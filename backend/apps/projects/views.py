from rest_framework import permissions, viewsets

from .models import Case
from .serializers import CaseInfoSerializer, CaseSerializer


# Case Viewset


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.prefetch_related("types", "problems").all()

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CaseSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Case.objects.all()
        qs = qs.prefetch_related("types", "problems")
        qs = qs.filter(envoy_id=self.request.user.id)
        return qs

    def perform_create(self, serializer):
        serializer.save(envoy=self.request.user)

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CaseSerializer
        return CaseInfoSerializer
