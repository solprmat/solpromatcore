# Generated by Django 2.2.1 on 2019-06-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0005_pregunta1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta1',
            name='respuesta',
            field=models.CharField(max_length=255),
        ),
    ]