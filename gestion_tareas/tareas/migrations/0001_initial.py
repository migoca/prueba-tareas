# Generated by Django 5.1.7 on 2025-03-10 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en progreso', 'En progreso'), ('completada', 'Completada')], default='pendiente', max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.familia')),
            ],
        ),
    ]
