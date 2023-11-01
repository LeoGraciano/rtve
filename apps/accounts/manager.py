from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.db.models import Manager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(
        self, email: str, password, is_staff: bool, is_superuser: bool, **kwargs
    ):
        now = timezone.now()
        if not email:
            raise ValueError(_("Um email válido deve ser informado."))

        name = kwargs.get("name").strip()
        if not name:
            raise ValidationError("name deve ser informado")

        email = email.strip().lower()

        phone_number = kwargs.get("phone_number")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            name=name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **kwargs):
        return self._create_user(email, password, False, False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        user = self._create_user(email, password, True, True, **kwargs)
        user.is_active = True
        user.save(using=self._db)
        return user


class UserClientManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(user_access__access="client")
        )


class UserEmployeeManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(user_access__access="employee")
        )
