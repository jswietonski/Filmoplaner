from django import forms
from zadanie.models import Zadanie

class ZadanieForm(forms.ModelForm):
    class Meta:
        model = Zadanie
        fields = "__all__"
