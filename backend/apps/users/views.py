from django.contrib.auth import authenticate, login

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserWriteSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UserSerializer
        return UserWriteSerializer

    def perform_update(self, serializer):
        user = serializer.save()
        if "password" in self.request.data:
            user.set_password(self.request.data.get("password"))
        user.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @action(methods=["GET"], detail=False)
    def me(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=["POST"], detail=False)
    def login(self, request, format=None):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
