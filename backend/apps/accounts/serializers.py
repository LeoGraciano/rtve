from rest_framework import serializers

from apps.accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ["url", "name", "email", "password", "is_staff"]
