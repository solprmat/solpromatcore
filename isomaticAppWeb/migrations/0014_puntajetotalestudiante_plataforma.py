# Generated by Django 2.2.1 on 2019-07-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0013_puntajetotalestudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntajetotalestudiante',
            name='plataforma',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
