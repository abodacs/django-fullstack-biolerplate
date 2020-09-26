from rest_framework import exceptions, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Confirmation, Patch
from .serializers import ConfirmationInfoSerializer, EnvoyPatchesSerializer


# Patch Viewset


class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    envoy_serializer_class = EnvoyPatchesSerializer

    @action(methods=["GET"], detail=False)
    def my_patches(self, request):
        if request.user.is_authenticated and request.user.is_active:
            qs = Patch.objects.prefetch_related("project__envoys").filter(
                project__envoys__in=[request.user.id]
            )
            qs = qs.order_by("-date")[:100]
            serializer = self.envoy_serializer_class(qs, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ConfirmationViewSet(viewsets.ModelViewSet):
    queryset = Confirmation.objects.all()

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    confirmation_serializer_class = ConfirmationInfoSerializer

    @action(methods=["GET"], detail=False)
    def my_confirmations(self, request):
        if request.user.is_authenticated and request.user.is_active:
            qs = Confirmation.objects.select_related("project", "case").filter(
                envoy_id__in=[request.user.id]
            )
            serializer = self.confirmation_serializer_class(qs, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def change_deliver_status(self, envoy_id, delivered=True):
        instance = self.get_object()
        if instance.envoy_id == envoy_id:
            instance.delivered = delivered
            instance.save(update_fields=["delivered"])
        else:
            raise exceptions.PermissionDenied()

    @action(detail=True, methods=["POST"])
    def confirm(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active:
            self.change_deliver_status(request.user.id)
            return Response(status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True, methods=["POST"])
    def cancel(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active:
            self.change_deliver_status(request.user.id, delivered=False)
            return Response(status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
