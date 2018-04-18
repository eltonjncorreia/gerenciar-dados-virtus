# Generated by Django 2.0.4 on 2018-04-17 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180417_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d+$')], verbose_name='telefone'),
        ),
    ]