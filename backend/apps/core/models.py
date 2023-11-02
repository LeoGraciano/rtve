from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class DateModelField(models.Model):
    """Classe de composição para modelos que utilizaram os
    campos created_at, updated_at
    """

    created_at = models.DateTimeField(
        _("Criado em"), auto_now_add=True, db_column="created_at"
    )
    updated_at = models.DateTimeField(
        _("Aualizado em"), auto_now=True, db_column="updated_at"
    )

    class Meta:
        abstract = True


class BaseModelField(DateModelField):
    """Classe de composição para modelos que utilizaram os
    campos uuid, is_active, created_at, updated_at
    """

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    is_active = models.BooleanField(
        _("Ativo"),
        default=True,
    )

    class Meta:
        abstract = True
