# Generated by Django 2.0.4 on 2018-04-17 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Valor',
            new_name='valor_total',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='total',
        ),
    ]
