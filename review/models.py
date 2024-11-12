from django.db import models
from product.models import Product
from user.models import Client
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Review(models.Model):
    reviewingClient = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Reviewing Client"))
    productReviewed = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product Reviewed"))
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Rating")
    )
    comment = models.CharField(max_length=250, verbose_name=_("Comment"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))

    class Meta:
        ordering = ['date']
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return _('{product} review by {client}').format(
            product=self.productReviewed.name,
            client=self.reviewingClient.user.first_name
        )
