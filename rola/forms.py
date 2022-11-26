from django import forms
from rola.models import Rola
from gatunek_filmu.models import GatunekFilmu

"""
class FilmForm(forms.Form):
    nazwa = forms.CharField(required=True)
    budzet = forms.CharField(required=False)
    id_gatunek = forms.ModelChoiceField(queryset=GatunekFilmu.objects.all())
    ograniczenie_wiekowe = forms.CharField(required=False)
    data_premiery = forms.CharField(required=False)

    #GatunekFilmu.objects.all().values_list('gatunekk', flat=True)
"""

class RolaForm(forms.ModelForm):
    class Meta:
        model = Rola
        fields = "__all__"
