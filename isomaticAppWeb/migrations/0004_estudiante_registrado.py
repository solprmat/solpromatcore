# Generated by Django 2.2.1 on 2019-06-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0003_remove_estudiante_registrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='registrado',
            field=models.BooleanField(default=False),
        ),
    ]