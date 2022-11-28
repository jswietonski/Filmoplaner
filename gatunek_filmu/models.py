from django.db import models

# Create your models here.


class GatunekFilmu(models.Model):
    '''Definicja tabeli gatunku w bazie danych'''
    gatunekk = models.CharField(max_length=40, default=None, blank=True, null=True, unique=True)

    class Meta:
        db_table = "gatunekfilmu"
    def __str__(self):
       return  self.gatunekk