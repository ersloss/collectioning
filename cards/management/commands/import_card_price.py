import ast
import urllib

from decimal import Decimal
from django.core.management import BaseCommand

from cards.models import Card


class Command(BaseCommand):
    help = 'Imports card data'

    def handle(self, *args, **options):
        needs_price = Card.objects.filter(price=Decimal('0.00')).first()

        # We're going to try not to abuse this API so only call once per call to this command
        if needs_price:
            request_str = ('http://magictcgprices.appspot.com/api/cfb/price.json?cardname=%s' %
                           needs_price.name.replace(' ', '%20'))
            url_resp = urllib.urlopen(request_str)
            if url_resp:
                price_info = url_resp.read()
                price_list = ast.literal_eval(price_info)
                if len(price_list):
                    try:
                        needs_price.price = Decimal(price_list[0].replace('$', ''))
                    except Exception as e:
                        print 'Error setting price to Decimal for card %s: %s' % (needs_price.name, e)
                    else:
                        print 'Got price for %s' % needs_price
                        needs_price.save()
                else:
                    print 'Could not get list literal from URL response.'
            else:
                print 'Could not get a URL response from request.'
