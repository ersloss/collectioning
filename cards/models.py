from __future__ import unicode_literals
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=150)
    mana_cost = models.CharField(max_length=50)
    cmc = models.IntegerField()
    type = models.CharField(max_length=100)
    text = models.TextField()
    power = models.CharField(max_length=5, blank=True, null=True)
    toughness = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)
    card = models.ForeignKey(to=Card, related_name='CardColor')


class CardType(models.Model):
    name = models.CharField(max_length=30)
    card = models.ForeignKey(to=Card, related_name='CardType')


class CardSubTypes(models.Model):
    name = models.CharField(max_length=30)
    card = models.ForeignKey(to=Card, related_name='CardSubtype')
