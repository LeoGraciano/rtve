from rest_framework import viewsets

from apps.expenditure.models import Expense
from apps.expenditure.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expenditure to be viewed or edited.
    """

    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
