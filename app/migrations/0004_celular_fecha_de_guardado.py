# Generated by Django 5.1.2 on 2024-10-31 20:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_celular_tiempo_de_uso'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='fecha_de_guardado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
