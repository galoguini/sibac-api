# Generated by Django 5.0.3 on 2024-06-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.CharField(default='Argentina', max_length=50),
            preserve_default=False,
        ),
    ]
