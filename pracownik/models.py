from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint


class Pracownik(models.Model):
    '''Definicja tabeli pracownik w bazie danych'''
    imie = models.CharField(max_length=20, default=None, blank=True, null=True)
    nazwisko = models.CharField(max_length=100, default=None, blank=True, null=True)
    data_zatrudnienia = models.CharField(max_length=30, default=None, blank=True, null=True)
    wynagrodzenie = models.CharField(max_length=20, default=None, blank=True, null=True)
    rola = models.CharField(max_length=30, default=None, blank=True, null=True)
    data_urodzenia = models.CharField(max_length=30, default=None, blank=True, null=True)
    econtact = models.CharField(max_length=15, default=None, blank=True, null=True)
    eemail = models.EmailField(default=None)
    #userr = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='id_usera', to_field='first_name')

    class Meta:
        db_table = "pracownik"
        #constraints = [
        #    UniqueConstraint('nazwisko', 'imie', 'id', name='labell')
        #]

    def __str__(self):
        return (str(self.id) + " " + self.imie + " " + self.nazwisko)
