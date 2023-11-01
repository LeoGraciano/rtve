from django_filters import rest_framework as filters
from rest_framework import viewsets

from apps.expenditure.filters import ExpenseFilter
from apps.expenditure.models import Expense
from apps.expenditure.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expenditure to be viewed or edited.
    """

    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter
