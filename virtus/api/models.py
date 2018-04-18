from django.db import models

from virtus.core.models import Cliente


class Pedido(models.Model):
    numero = models.IntegerField('numero')
    data = models.DateField('data', auto_now_add=True)
    loja = models.CharField('loja', max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_total = models.DecimalField('valor Total', max_digits=10, decimal_places=2,)

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
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.descricao
