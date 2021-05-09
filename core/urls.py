from django.urls import path

from core.views import get_numbers_list, get_country

urlpatterns = [
    path('', get_numbers_list, name='number_list'),
    path('country/<str:name>', get_country, name='country')
]
