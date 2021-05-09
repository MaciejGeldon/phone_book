from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from core.models import Entry, Country


def get_numbers_list(request):
    numbers_list = Entry.objects.all().select_related('country')
    return render(
        request,
        'core/phone_number_list.html',
        {'phone_numbers': numbers_list}
    )


def get_country(request, name):
    country = get_object_or_404(Country, name=name)

    return render(
        request,
        'core/country.html',
        {'country': country}
    )

