from django import forms
from studio.models import Studio


class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = "__all__"

