from django import forms
from ..models import Contato

class InformacaoContatoForm(forms.ModelForm):
    contato_nome_input = forms.CharField(
        label='Nome', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    contato_email_input = forms.CharField(
        label='E-mail', 
        max_length=200, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    contato_telefone_input = forms.CharField(
        label='Telefone', 
        max_length=16, 
        widget=forms.TextInput(attrs={'placeholder': 'Telefone'})
    )
    contato_empresa_input = forms.CharField(
        label='Empresa', 
        max_length=60, 
        widget=forms.TextInput(attrs={'placeholder': 'Empresa'})
    )
    class Meta:
        model = Contato
        fields = ['contato_nome_input', 'contato_email_input', 'contato_telefone_input', 'contato_empresa_input']


# class IncluirContato(forms.Form):
 