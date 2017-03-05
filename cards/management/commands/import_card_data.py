import json
import os
import re

from django.core.management import BaseCommand
from django.db import DataError

from cards.models import Card, Color, CardType, CardSubTypes
from collectioning.settings import IMPORT_DIR

full_card_file = os.path.join(IMPORT_DIR, 'AllCards.json')


class Command(BaseCommand):
    help = 'Imports card data'

    def handle(self, *args, **options):
        with open(full_card_file) as cards_json:
            all_cards = json.load(cards_json)

        for card in all_cards.iteritems():
            name = card[1].get('name', 'LAME')
            mana_cost = card[1].get('manaCost', 'LAME')
            cmc = card[1].get('cmc', 0)
            color = card[1].get('colors')
            card_type = re.sub(r'\W+', ' ', card[1].get('type'))
            card_types = card[1].get('types')
            card_subtypes = card[1].get('subtypes')
            text = card[1].get('text', '')
            power = card[1].get('power')
            toughness = card[1].get('toughness')

            # Make and save the new card first, we'll add the color, type and subtype references later
            try:
                new_card, created = Card.objects.get_or_create(
                    name=name, mana_cost=mana_cost, cmc=cmc, type=card_type, text=text)
            except DataError as de:
                print 'Error creating new card %s: %s' % (name, de)

            if new_card and power:
                new_card.power = power

            if new_card and toughness:
                new_card.toughness = toughness

            new_card.save()

            # Make or get each color object for each card
            if color:
                for each_color in color:
                    card_color, created = Color.objects.get_or_create(name=each_color, card=new_card)
                    card_color.save()

            # Make or get each color object for each card
            if card_types:
                for each_type in card_types:
                    card_type, created = CardType.objects.get_or_create(name=each_type, card=new_card)
                    card_type.save()

            if card_subtypes:
                # Make or get each color object for each card
                for each_subtype in card_subtypes:
                    card_subtype, created = CardSubTypes.objects.get_or_create(name=each_subtype, card=new_card)
                    card_subtype.save()
