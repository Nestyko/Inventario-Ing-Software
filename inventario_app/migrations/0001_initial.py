# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 00:26
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
            name='Cliente',
            fields=[
                ('cedula', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=15)),
                ('telefono_alternativo', models.CharField(blank=True, max_length=15, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('codigo', models.PositiveIntegerField()),
                ('proveedor', models.CharField(max_length=100)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField(blank=True, null=True)),
                ('stock', models.PositiveIntegerField()),
                ('stock_minimo', models.PositiveIntegerField(blank=True, null=True)),
                ('stock_maximo', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.ManyToManyField(to='inventario_app.Producto'),
        ),
    ]
