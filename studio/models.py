from django.db import models
from mapbox_location_field.models import LocationField

# Create your models here.


class Studio(models.Model):
    '''Definicja tabeli studio w bazie danych'''
    nazwa = models.CharField(max_length=40, default=None, blank=True, null=True, unique=True)
    adres= models.CharField(max_length=2000, default=None, blank=True, null=True)
    powierzchnia = models.CharField(max_length=40, default=None, blank=True, null=True)
    location = LocationField(null= True, map_attrs={"center": [21.017532, 52.237049]})

    class Meta:
        db_table = "studio"

    def __str__(self):
        return self.nazwa