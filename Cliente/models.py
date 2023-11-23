from django.db import models

class Cliente(models.Model):

    razaosocial = models.CharField(max_length=100, blank=True)
    cnpj= models.CharField(max_length=21, blank=True)
    inscestadual = models.CharField(max_length=15, blank=True)

    nome = models.CharField(max_length=100, blank=True)
    cpf= models.CharField(max_length=16 , blank=True)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20, null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    tipo = models.CharField(max_length=2)


    def __str__(self) -> str:
        return super().__str__()