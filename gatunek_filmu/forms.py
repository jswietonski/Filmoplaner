from django import forms
from gatunek_filmu.models import GatunekFilmu


class GatunekFilmuForm(forms.ModelForm):
    class Meta:
        model = GatunekFilmu
        fields = "__all__"
