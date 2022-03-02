from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from user.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    staff_id = models.ForeignKey(
        to="apis.Staff", on_delete=models.CASCADE, blank=True, null=True)

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        max_length=64, verbose_name=_('username'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    remarks = models.CharField(max_length=1024, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
