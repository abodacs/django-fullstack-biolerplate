from django.contrib.auth import get_user_model

from apps.users.serializers import LogInSerializer, UserSerializer, UserWriteSerializer
from rest_framework import parsers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

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
        if request.user.is_authenticated and request.user.is_active:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
