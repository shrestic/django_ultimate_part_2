from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    # Because birth_date not exist in User(AbstractUser) model, we need to add it here
    birth_date = serializers.DateField()

    class Meta(BaseUserCreateSerializer.Meta):
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            # "birth_date"
        )


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )
