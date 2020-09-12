from rest_framework import permissions, viewsets

from .serializers import CaseSerializer


# Case Viewset


class CaseViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CaseSerializer

    def get_queryset(self):
        return self.request.user.cases.all()

    def perform_create(self, serializer):
        serializer.save(envoy=self.request.user)
