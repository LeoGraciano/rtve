from apps.core.models import BaseModelField
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Expense(BaseModelField):
    description = models.CharField(_("Despesa"), max_length=50)
    date = models.DateField(_("Data"), auto_now=False, auto_now_add=False)
    value = models.DecimalField(_("Valor"), max_digits=10, decimal_places=2)

    categories = models.ManyToManyField(
        "categories.Category",
        verbose_name="Categorias",
        related_name="expenditure",
    )

    created_by = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Criado por"),
        on_delete=models.CASCADE,
        related_name="created_by_expense",
        blank=True,
        null=True,
        editable=False,
    )

    def get_categories(self) -> list:
        try:
            categories = self.categories.all()
            if categories.exists():
                return [str(x.name) for x in categories]
        except Exception:
            pass

        return []

    def __str__(self):
        return f"{self.description} - {self.date.strftime('%d/%m/%Y')} - {self.value}"

    class Meta:
        db_table = "tb_expense"
        verbose_name = _("Despesa")
        verbose_name_plural = _("Despesas")
