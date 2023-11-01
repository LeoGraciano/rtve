from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModelField


# Create your models here.
class Category(BaseModelField):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_category"
        ordering = ["name"]
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")
