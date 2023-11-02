from rest_framework import viewsets

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
