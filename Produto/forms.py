from django import forms

from Produto.models import Produto


class ProdutoForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codBarras'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['valorCompra'].widget.attrs.update({'class': 'form-control'})
        self.fields['valorVenda'].widget.attrs.update({'class': 'form-control'})
        self.fields['img'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Produto
        fields = ['codBarras', 'descricao', 'valorCompra', 'valorVenda', 'img']


class ProdutoEditForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codBarras'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['valorCompra'].widget.attrs.update({'class': 'form-control'})
        self.fields['valorVenda'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Produto
        fields = ['codBarras', 'descricao', 'valorCompra', 'valorVenda']

# codBarras = models.CharField(max_length=50)
#     descricao = models.CharField(max_length=50)
#     valorCompra = models.DecimalField(max_digits=8, decimal_places=2)
#     valorVenda = models.DecimalField(max_digits=8, decimal_places=2)
#     img = models.ImageField(upload_to='images/')
#     status = models.BooleanField(default=True);
        