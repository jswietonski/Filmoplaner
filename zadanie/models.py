from django.db import models

# Create your models here.
from pracownik.models import Pracownik
from menadzer.models import Menadzer
from film.models import Film
from django.db import models

# Create your models here.



class Zadanie(models.Model):
    '''Definicja tabeli zadanie w bazie danych'''
    id_pracownik = models.ForeignKey(Pracownik, null=True, on_delete=models.DO_NOTHING, related_name='id_pracownika'
                                   )
    id_menadzer = models.ForeignKey(Menadzer, null=True, on_delete=models.DO_NOTHING, related_name='id_menadzera'
                                   )
    id_film = models.ForeignKey(Film, null=True, on_delete=models.DO_NOTHING, related_name='id_ffilmu',
                                   to_field='nazwa')
    tytul = models.CharField(max_length=100, default=None, blank=True, null=True, unique=False)
    opis = models.CharField(max_length=255, default=None, blank=True, null=True )
    termin = models.CharField(max_length=20, default=None, blank=True, null=True, unique=False)

    class Meta:
        db_table = "zadanie"

    def __str__(self):
        return self.tytul
