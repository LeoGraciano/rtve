from apps.categories.serializers import CategorySerializer
from apps.expenditure.models import Expense
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    categories = CategorySerializer

    categories_display = serializers.SerializerMethodField(read_only=True)

    def save(self, *args, **kwargs):
        instance = super(ExpenseSerializer, self).save(*args, **kwargs)
        request = self.context.get("request")
        if request.user.is_authenticated and instance.created_by is None:
            instance.created_by = request.user
            instance.save()

        return instance

    def get_created_by(self, instance):
        try:
            return instance.created_by.name
        except Exception:
            return ""

    def get_categories_display(self, instance):
        return ", ".join(instance.get_categories())

    class Meta:
        model = Expense
        fields = [
            "url",
            "uuid",
            "description",
            "date",
            "value",
            "categories",
            "categories_display",
            "created_by",
            "is_active",
        ]
