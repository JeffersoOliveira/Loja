from collections.abc import Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Cliente


class ClientePfForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone','cpf', 'email', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'tipo']


        

class ClientePjForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razaosocial', 'telefone','cnpj', 'inscestadual', 'email', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'tipo']

