import pytest
from django.urls import reverse
from core.factories import EntryFactory, CountryFactory


@pytest.mark.django_db
def test_if_phone_number_added_correctly():
    example_entry = EntryFactory()

    prefix = example_entry.country.prefix
    local_part = example_entry.local_number

    assert example_entry.full_number == f'{prefix} {local_part}'


@pytest.mark.django_db
@pytest.mark.parametrize(
    'resp_length', [
        1, 2
    ]
)
def test_django_template_view_single_entry(client, resp_length):
    for i in range(resp_length):
        EntryFactory()

    response = client.get(reverse('core:number_list'))

    assert response.status_code == 200
    assert 'phone_numbers' in response.context
    assert len(response.context['phone_numbers']) == resp_length


@pytest.mark.django_db
def test_country_detail(client):
    country = CountryFactory()

    response = client.get(reverse('core:country', kwargs={'name': country.name}))

    assert response.status_code == 200
    assert 'country' in response.context
    assert response.context['country'].name == country.name
    assert response.context['country'].prefix == country.prefix


@pytest.mark.django_db
def test_country_detail_not_found(client):
    response = client.get(reverse('core:country', kwargs={'name': 'non exisitng'}))

    assert response.status_code == 404
