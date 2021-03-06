import string
import factory.fuzzy

from core.models import Country, Entry


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Country

    prefix = factory.Sequence(lambda n: f'+ {n}')
    name = factory.Sequence(lambda n: f'Test country {n}')


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    country = factory.SubFactory(CountryFactory)
    name = factory.Sequence(lambda n: f'Company {n} sp z.o.o')
    description = 'Some description'
    local_number = factory.fuzzy.FuzzyText(length=9, chars=string.digits)
