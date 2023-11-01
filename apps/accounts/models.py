from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.accounts.manager import UserManager
from apps.core.models import BaseModelField


class User(AbstractBaseUser, PermissionsMixin, BaseModelField):
    email = models.EmailField(_("E-mail"), unique=True, db_column="email")
    name = models.CharField(_("Nome completo"), max_length=150, db_column="name")
    phone_number = models.CharField(
        _("Telefone celular"),
        max_length=11,
        validators=[
            RegexValidator(regex=r"^[1-9]{2}9[0-9]{8}$", message=_("Telefone inválido"))
        ],
        blank=True,
        null=True,
        db_column="phone_number",
    )
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    is_trusty = models.BooleanField(default=False)
    confirmation_key = models.CharField(
        max_length=24, blank=True, null=True, db_column="confirmation_key"
    )

    updated_at = models.DateField("Updated in", auto_now=True, db_column="updated_at")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def get_short_name(self):
        return self.name.split(" ")[0]

    def save(self, *args, **kwargs):
        self.full_clean()  # Verifica as restrições extras de cada field
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "tb_user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
