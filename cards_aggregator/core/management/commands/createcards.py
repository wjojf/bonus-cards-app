from django.core.management.base import BaseCommand
from core.models import Card
from core.utils import getDateFromShortString
from random import choice 


class Command(BaseCommand):

    SERIES_MIN, SERIES_MAX = 4518, 4520
    NUMBER_MIN, NUMBER_MAX = 1000, 1010
    ACTIVE_STATUS = Card.STATUS_OPTS[0][0]
    YEAR_ACTIVE_DATE = getDateFromShortString('1y')
    YEAR_3_ACTIVE_DATA = getDateFromShortString('3y')
    YEAR_5_ACTIVE_DATA = getDateFromShortString('5y')



    def handle(self, *args, **options):
        for series in range(self.SERIES_MIN, self.SERIES_MAX + 1):
            for number in range(self.NUMBER_MIN, self.NUMBER_MAX + 1):
                card_obj, created = Card.objects.get_or_create(
                    series=series,
                    number=number,
                    status=self.ACTIVE_STATUS,
                    date_expired=choice((self.YEAR_ACTIVE_DATE, self.YEAR_3_ACTIVE_DATA, self.YEAR_5_ACTIVE_DATA))
                )
                print(f'Created {card_obj}')
                card_obj.save()
