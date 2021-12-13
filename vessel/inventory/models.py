from django.contrib.auth import get_user_model
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from vessel.core.models import ModelBase


# Create your models here.
class Inventory(ModelBase):
    name = models.CharField("name", max_length=64, help_text="Item name.")
    qtd = models.IntegerField("quantity", help_text="Item quantity.")

    class Meta:
        verbose_name = "receita"
        verbose_name_plural = "receitas"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Recipe({model_to_dict(self)})"

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False
    )
