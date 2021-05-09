from django.shortcuts import render

# Create your views here.
from core.models import Entry


def get_numbers_list(request):
    numbers_list = Entry.objects.all().select_related('country')
    return render(
        request,
        'core/phone_number_list.html',
        {'phone_numbers': numbers_list}
    )
