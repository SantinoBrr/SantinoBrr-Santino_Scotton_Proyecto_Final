# Generated by Django 5.1.2 on 2024-10-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='tiempo_de_uso',
            field=models.IntegerField(help_text='Tiempo de uso en meses'),
        ),
    ]
