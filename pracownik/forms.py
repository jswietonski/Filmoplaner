from django import forms
from pracownik.models import Pracownik


class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = "__all__"