from core.factories import EntryFactory
import pytest


@pytest.mark.django_db
def test_if_phone_number_added_correctly():
    example_entry = EntryFactory()

    prefix = example_entry.country.prefix
    local_part = example_entry.local_number

    assert example_entry.full_number == f'{prefix} {local_part}'
