from django.db import models

# Create your models here.

from studio.models import Studio
from film.models import Film
from django.db import models

# Create your models here.



class Spotkanie(models.Model):
    '''Definicja tabeli spotkanie w bazie danych'''
    tytul = models.CharField(max_length=100, default=None, blank=True, null=True)
    id_film = models.ForeignKey(Film, null=True, on_delete=models.DO_NOTHING, related_name='id_filmu', to_field='nazwa')
    id_lokalizacja = models.ForeignKey(Studio, null=True, on_delete=models.DO_NOTHING, related_name='id_studia',
                                   to_field='nazwa')
    data_rozpoczecia = models.CharField(max_length=30, default=None, blank=True, null=True)
    godzina = models.TimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "spotkanie"

