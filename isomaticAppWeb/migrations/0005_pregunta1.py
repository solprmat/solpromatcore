# Generated by Django 2.2.1 on 2019-06-16 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isomaticAppWeb', '0004_estudiante_registrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=1)),
                ('fecha_registro_P01', models.DateTimeField(auto_now_add=True)),
                ('preguntaGuardada', models.BooleanField(default=False)),
                ('identificadorEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta1', to='isomaticAppWeb.Estudiante')),
            ],
        ),
    ]
