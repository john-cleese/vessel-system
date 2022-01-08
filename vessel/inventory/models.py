from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from vessel.core.models import ModelBase


# Create your models here.
class Item(ModelBase):
    name = models.CharField("name", max_length=64, help_text="Item name.")
    qtd = models.IntegerField("quantity", help_text="Item quantity.")

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item{model_to_dict(self)})"

    def get_absolute_url(self):
        return reverse("api:item-detail", kwargs={"pk": self.pk})
