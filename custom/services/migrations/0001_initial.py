# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-12-15 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gui', '0003_auto_20180916_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('fees', models.FloatField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('is_available', models.NullBooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Service Package',
                'verbose_name_plural': 'Service Packages',
            },
        ),
        migrations.CreateModel(
            name='PackageNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='services.Package')),
            ],
            options={
                'ordering': ['package'],
                'verbose_name': 'Package Note',
                'verbose_name_plural': 'Package Notes',
            },
        ),
        migrations.CreateModel(
            name='PackageTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Package Term',
                'verbose_name_plural': 'Package Terms',
            },
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Package Type',
                'verbose_name_plural': 'Packate Types',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('fees', models.FloatField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('is_available', models.NullBooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='package_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.PackageType'),
        ),
        migrations.AddField(
            model_name='package',
            name='services',
            field=models.ManyToManyField(related_name='services', to='services.Service'),
        ),
        migrations.AddField(
            model_name='package',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gui.State'),
        ),
        migrations.AlterUniqueTogether(
            name='packagenote',
            unique_together=set([('package', 'note')]),
        ),
    ]
