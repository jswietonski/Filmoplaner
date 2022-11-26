from django import forms
from aktor.models import Aktor
class AktorForm(forms.ModelForm):
    class Meta:
        model = Aktor
        fields = "__all__"