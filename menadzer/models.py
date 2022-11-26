from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Menadzer(models.Model):
    '''Definicja tabeli pracownik w bazie danych'''
    imie = models.CharField(max_length=20, default=None, blank=True, null=True)
    nazwisko = models.CharField(max_length=100, default=None, blank=True, null=True)
    nrtel = models.CharField(max_length=15, default=None, blank=True, null=True)
    eemail = models.EmailField(default=None)
    data_urodzenia = models.CharField(max_length=30, default=None, blank=True, null=True)
    data_zatrudnienia = models.CharField(max_length=30, default=None, blank=True, null=True)
    wynagrodzenie = models.CharField(max_length=20, default=None, blank=True, null=True)

    class Meta:
        db_table = "menadzer"

    def __str__(self):
        return (str(self.id) +" " +self.imie + " " + self.nazwisko)

