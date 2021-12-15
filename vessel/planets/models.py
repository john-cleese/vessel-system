from datetime import datetime
from django.db import models

from vessel.core.models import ModelBase
from vessel.users.models import User



class Planet(ModelBase):
    name = models.CharField(
        max_length=60,
        verbose_name='Name'
    )
    total_area = models.DecimalField(
        verbose_name='Total Area',
        max_digits=9,
        decimal_places=2
    )
    population = models.IntegerField(
        verbose_name='Population',
    )
    discovery_date = models.DateTimeField(
        verbose_name='Discovery Date',
        blank=True
    )

    @property
    def age(self):
        age = self.discovery_date - datetime.datetime.now()
        return age

    class Meta:
        verbose_name = "Planet"
        verbose_name_plural = "Planets"
        ordering = ["id", ]

    def __str__(self):
        return self.name
