from django.db import models

# Create your models here.


class Studio(models.Model):
    '''Definicja tabeli studio w bazie danych'''
    nazwa = models.CharField(max_length=40, default=None, blank=True, null=True, unique=True)
    lat = models.FloatField( default=None, blank=True, null=True)
    lon = models.FloatField( default=None, blank=True, null=True)
    powierzchnia = models.CharField(max_length=40, default=None, blank=True, null=True)

    class Meta:
        db_table = "studio"

    def __str__(self):
        return self.nazwa