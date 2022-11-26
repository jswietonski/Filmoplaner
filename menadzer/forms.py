from django import forms
from menadzer.models import Menadzer
class MenadzerForm(forms.ModelForm):
    class Meta:
        model = Menadzer
        fields = "__all__"