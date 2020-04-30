from django.db import models

class App(models.Model):

    STATUS = (
        ('indisponivel', 'Indisponivel'),
        ('disponivel', 'Disponivel'),
    )

    nome = models.CharField(max_length = 255)
    descricao = models.TextField()
    disponivel = models.CharField(max_length = 12, choices=STATUS,)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome 