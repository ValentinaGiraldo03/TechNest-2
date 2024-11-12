from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    pass

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))

    class Meta:
        verbose_name = _("Administrator")
        verbose_name_plural = _("Administrators")
