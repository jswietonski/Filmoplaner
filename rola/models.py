from django.db import models

# Create your models here.

from aktor.models import Aktor
from film.models import Film
from django.db import models

# Create your models here.



class Rola(models.Model):
    '''Definicja tabeli rola w bazie danych'''
    id_film = models.ForeignKey(Film, null=True, on_delete=models.DO_NOTHING)
    id_aktor = models.ForeignKey(Aktor, null=True, on_delete=models.DO_NOTHING)
    tytul = models.CharField(max_length=100, default=None, blank=True, null=True)
    typ_roli = models.CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        db_table = "rola"

