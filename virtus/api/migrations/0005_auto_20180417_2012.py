# Generated by Django 2.0.4 on 2018-04-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_item_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor Total'),
        ),
    ]
