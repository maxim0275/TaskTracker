from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class TTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer выдачи токена."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email

        return token


class UserSerializer(ModelSerializer):
    """Serializer модели пользователя."""

    class Meta:
        model = User
        fields = ("id", "email", "phone")
