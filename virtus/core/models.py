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


class Pedido(models.Model):
    numero = models.IntegerField('numero')
    data = models.DateField('data', auto_now_add=True)
    loja = models.CharField('loja', max_length=255)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    valor_total = models.DecimalField('valor', max_digits=10, decimal_places=2,)

    class Meta:
        ordering = ['numero']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.loja


class Item(models.Model):
    codigo = models.IntegerField('codigo')
    descricao = models.CharField('descricao', max_length=255)
    valor = models.DecimalField('valor', max_digits=10, decimal_places=2,)
    unitario = models.DecimalField('Unitário', max_digits=10, decimal_places=2)
    quantidade = models.IntegerField('quantidade')

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.descricao
