from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)

    def get_full_name(self, obj):
        return obj.full_name

    def get_short_name(self, obj):
        return obj.short_name

    class Meta:
        model = User
        fields = ["username", "name", "short_name"]
        read_only_fields = fields


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["password", "name", "mobile"]


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != "id":
                token[key] = value
        return token
