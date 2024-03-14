from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    #Adiciconado por Kaua
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=True)
    def __str__(self):
        return self.descricao, self.nome
    



