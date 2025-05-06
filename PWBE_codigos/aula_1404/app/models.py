from django.db import models

# Create your models here.
class Piloto(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveBigIntegerField()
    classificacao = models.PositiveBigIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} está na {self.classificacao} posição'

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca  = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveBigIntegerField()
    escolha_cores = (
        ("VERMELHO", "Vermelho"),
        ("ROSA", "Rosa"), 
        ("BRANCO", "Branco"),
        ("PRETO", "Preto"),
        ("VERDE", "Verde"),
    )
    cor = models.CharField(max_length=50, choices=escolha_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)