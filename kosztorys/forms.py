from django import forms
from kosztorys.models import Kosztorys


class KosztorysForm(forms.ModelForm):
    class Meta:
        model = Kosztorys
        fields = "__all__"
