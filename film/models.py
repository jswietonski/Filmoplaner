from django.db import models

# Create your models here.
from gatunek_filmu.models import GatunekFilmu
from django.db import models

# Create your models here.



class Film(models.Model):
    '''Definicja tabeli film w bazie danych'''
    nazwa = models.CharField(max_length=20, default=None, blank=True, null=True, unique=True)
    budzet = models.IntegerField(default=None, blank=True, null=True)
    id_gatunek = models.ForeignKey(GatunekFilmu, null=True, on_delete=models.DO_NOTHING, related_name='id_gatunku', to_field='gatunekk')
    ograniczenie_wiekowe = models.CharField(max_length=20, default=None, blank=True, null=True)
    data_premiery = models.CharField(max_length=30, default=None, blank=True, null=True)

    class Meta:
        db_table = "film"

    def __str__(self):
        return self.nazwa
