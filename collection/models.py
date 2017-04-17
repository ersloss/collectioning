from __future__ import unicode_literals

from decimal import Decimal
from django.db import models

from cards.models import Card


class Collection(models.Model):
    name = models.CharField(max_length=150)
    cards = models.ManyToManyField(Card)
    total_value = models.DecimalField(decimal_places=2, max_digits=30, default=Decimal('0.00'))

    def __str__(self):
        return self.name
