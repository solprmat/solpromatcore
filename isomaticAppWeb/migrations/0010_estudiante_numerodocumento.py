# Generated by Django 2.2.1 on 2019-06-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0009_pregunta6'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='numeroDocumento',
            field=models.IntegerField(default=1, help_text='Ingrese su número de documento'),
            preserve_default=False,
        ),
    ]
