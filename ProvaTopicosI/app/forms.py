from django import forms 

from .models import App

class ProdutoForm(forms.ModelForm):

    class Meta:
        model= App
        fields = ('nome', 'descricao')