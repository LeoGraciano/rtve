from rest_framework import serializers

from apps.expenditure.models import Expense


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.SerializerMethodField()

    def save(self, *args, **kwargs):
        instance = super(ExpenseSerializer, self).save(*args, **kwargs)
        if instance.created_by is None:
            request = self.context.get("request")
            instance.created_by = request.user
            instance.save()

        return instance

    def get_created_by(self, instance):
        try:
            return instance.created_by.name
        except Exception:
            return ""

    class Meta:
        model = Expense
        fields = ["url", "description", "date", "value", "categories", "created_by"]
