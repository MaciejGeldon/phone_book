from django.urls import path

from core.views import get_numbers_list
urlpatterns = [
    path('', get_numbers_list, name='number_list'),
]
