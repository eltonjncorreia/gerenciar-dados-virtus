from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=255)
    email = models.EmailField('email', max_length=255)
    telefone = models.IntegerField('telefone')
    cpf = models.CharField('cpf', max_length=11, validators=[RegexValidator(r'^\d+$')])

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    TIPO = (
        ('R', 'Rua'),
        ('A', 'Av'),
        ('K', 'Km'),
        ('L', 'Lot'))

    tipo = models.CharField('tipo', choices=TIPO, max_length=1)
    cep = models.CharField('cep', max_length=8, validators=[RegexValidator(r'^\d+$')])
    rua = models.CharField('Rua', max_length=255)
    numero=models.IntegerField('numero')
    complemento = models.CharField('complemento', max_length=100)

    class Meta:
        ordering = ['tipo']
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.rua

