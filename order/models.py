from django.db import models
from user.models import Client
from product.models import Product
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Client"))
    products = models.ManyToManyField(Product, through='OrderProduct', verbose_name=_("Products"))
    state = models.CharField(max_length=25, verbose_name=_("State"))
    date = models.DateTimeField(verbose_name=_("Date"))
    total = models.FloatField(verbose_name=_("Total"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'{_("Order")} {self.id}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        unique_together = ('order', 'product')
        verbose_name = _("Order Product")
        verbose_name_plural = _("Order Products")

    def __str__(self):
        return f'{_("Order")} {self.order.id} - {_("Product")} {self.product.name}'
