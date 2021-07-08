from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('__all__')