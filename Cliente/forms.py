from django import forms
from .models import Cliente


class ClientePfForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone','cpf', 'email', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'tipo']

class ClientePjForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razaosocial', 'telefone','cnpj', 'inscestadual', 'email', 'cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'tipo']

