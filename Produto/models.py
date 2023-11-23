from django.db import models

# Create your models here.
class Produto(models.Model):

    codBarras = models.CharField(max_length=50, unique=True, verbose_name='Código de Barras')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valorCompra = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor da Compra ')
    valorVenda = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor da Venda' )
    img = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=True);

    def __str__(self):
        return self.descricao
    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.img.name = self.codBarras+'.'+self.img.name.split('.')[1] # Pegando a extensão da img
        super(Produto, self).save(*args, **kwargs)