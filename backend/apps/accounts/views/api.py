from rest_framework import viewsets

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
