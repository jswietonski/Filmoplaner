from django.db import models

# Create your models here.
from film.models import Film
from django.db import models

# Create your models here.



class Kosztorys(models.Model):
    '''Definicja tabeli kosztorys w bazie danych'''
    id_filmm = models.ForeignKey(Film, null=True, on_delete=models.DO_NOTHING, related_name='id_filmuu', to_field='nazwa')
    koszt_produkcji = models.IntegerField(default=None, blank=True, null=True)
    koszt_postprodukcji = models.IntegerField(default=None, blank=True, null=True)
    koszt_marketingu = models.IntegerField(default=None, blank=True, null=True)
    koszt_calkowity = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = "kosztorys"
