from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    prefix = models.CharField(max_length=16)

    def __str__(self):
        return f'Country(name={self.name}, prefix={self.prefix})'


class Entry(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    country = models.ForeignKey(Country, models.CASCADE)
    local_number = models.CharField(max_length=16, unique=True)

    @property
    def full_number(self):
        return f'{self.country.prefix} {self.local_number}'

    def __str__(self):
        return f'Entry(name={self.name}, country={self.country})'
