# Generated by Django 2.2.1 on 2019-06-13 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='registrado',
            field=models.BooleanField(default=bool),
        ),
    ]
