# Generated by Django 5.0.3 on 2024-04-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='empresa_entidad',
            field=models.CharField(max_length=100),
        ),
    ]
