from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    source = models.URLField(_("Website Link"), max_length=200)
    category = models.CharField(_("Category"), max_length=50, null=True, blank=True)
    brand = models.CharField(_("Brand"), max_length=250, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=250, null=True, blank=True)
    old_price = models.CharField(_("Price"), max_length=50, null=True, blank=True)
    discount = models.CharField(_("Discount"), max_length=150, null=True, blank=True)
    price = models.CharField(_("Price"), max_length=150, null=True, blank=True)

    image = models.URLField(_("Image link"), max_length=200, null=True, blank=True)

    detail_url = models.URLField(_("Detail Url"), max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.source} - {self.category if self.category else ''}"
