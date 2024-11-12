from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    PRODUCT_TYPES = [
        ("Computer", _("Computer")),
        ("Screen", _("Screen")),
        ("Keyboard", _("Keyboard")),
        ("Mouse", _("Mouse")),
        ("Printer", _("Printer")),
    ]
    
    name = models.CharField(max_length=30, null=False, verbose_name=_("Name"))
    description = models.CharField(max_length=1000, null=True, verbose_name=_("Description"))
    price = models.FloatField(null=False, validators=[MinValueValidator(0)], verbose_name=_("Price"))
    brand = models.CharField(max_length=20, null=True, verbose_name=_("Brand"))
    category = models.CharField(max_length=20, choices=PRODUCT_TYPES, verbose_name=_("Category"))
    stock = models.IntegerField(validators=[MinValueValidator(0)], verbose_name=_("Stock"))
    image = models.ImageField(null=True, upload_to='product/', verbose_name=_("Image"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
