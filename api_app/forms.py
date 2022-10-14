from django import forms
from . import models

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = '__all__'
        labels = {
            'slug':'Entrez votre Crypto ici',
            'convert':'Entrez votre Devise ici',
        }