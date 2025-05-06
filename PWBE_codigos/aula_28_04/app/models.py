from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)


# Abstratct User - usuário genérico
class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)

    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')), null=True, blank=True)

    escolha_colaborador = (
        ('G', 'Gestor'), 
        ('E', 'Estagiário'), 
        ('A', 'Aprendiz'), 
        ('M', 'Meio Oficial')
    )

    colaborador = models.CharField(max_length=1, choices=escolha_colaborador, default='M')

    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

class Ingresso(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


