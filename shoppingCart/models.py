from django.db import models
from product.models import Product
from user.models import Client
from django.utils.translation import gettext_lazy as _

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Quantity"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=Client.objects.first().id, verbose_name=_("Client"))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Added"))

    def __str__(self):
        return _('{quantity} x {product}').format(quantity=self.quantity, product=self.product.name)

    class Meta:
        verbose_name = _("Cart Product")
        verbose_name_plural = _("Cart Products")
