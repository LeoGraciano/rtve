from django_filters import rest_framework as filters

from apps.expenditure.models import Expense


class ExpenseFilter(filters.FilterSet):
    description = filters.CharFilter(
        label="Descrição",
        lookup_expr="icontains",
    )
    value_after = filters.NumberFilter(
        label="Valor de",
        lookup_expr="lte",
        field_name="value",
    )
    value_before = filters.NumberFilter(
        label="Valor até",
        lookup_expr="gte",
        field_name="value",
    )
    date_after = filters.DateFilter(
        label="Data de",
        lookup_expr="lte",
        field_name="date",
    )
    date_before = filters.DateFilter(
        label="Data até",
        lookup_expr="gte",
        field_name="date",
    )

    categories = filters.CharFilter(
        label="Categoria",
        field_name="categories__name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Expense
        fields = [
            "description",
            "value_after",
            "value_before",
            "date_after",
            "date_before",
        ]
