# Generated by Django 2.2.1 on 2019-07-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0010_estudiante_numerodocumento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='numeroDocumento',
        ),
    ]