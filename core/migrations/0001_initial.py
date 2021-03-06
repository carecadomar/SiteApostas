# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 23:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAposta', models.DateTimeField(verbose_name='dataaposta')),
                ('nome', models.CharField(max_length=200)),
                ('b1', models.CharField(max_length=2)),
                ('b2', models.CharField(max_length=2)),
                ('b3', models.CharField(max_length=2)),
                ('b4', models.CharField(max_length=2)),
                ('b5', models.CharField(max_length=2)),
                ('e1', models.CharField(max_length=2)),
                ('e2', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataConcurso', models.DateTimeField(verbose_name='dataconcurso')),
                ('b1', models.CharField(max_length=2)),
                ('b2', models.CharField(max_length=2)),
                ('b3', models.CharField(max_length=2)),
                ('b4', models.CharField(max_length=2)),
                ('b5', models.CharField(max_length=2)),
                ('e1', models.CharField(max_length=2)),
                ('e2', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.IntegerField(default=0)),
                ('nomeUtilizador', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('premios', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIF', models.IntegerField(null=True)),
                ('contacto', models.IntegerField(null=True)),
                ('codigopostal', models.IntegerField(null=True)),
                ('morada', models.CharField(max_length=200, null=True)),
                ('localidade', models.CharField(max_length=50, null=True)),
                ('pais', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='aposta',
            name='nConcurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Concurso'),
        ),
        migrations.AddField(
            model_name='aposta',
            name='nConta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Conta'),
        ),
    ]
