# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-18 12:53
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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_seen', models.NullBooleanField(default=False)),
                ('is_answered', models.NullBooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.CharField(blank=True, max_length=1000, null=True)),
                ('time_sent', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(blank=True, db_column='receiver', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, db_column='sender', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='MessagingSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duplicate_private', models.NullBooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Messaging Settings',
                'verbose_name_plural': 'Messaging Settings',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_received', models.NullBooleanField(default=False)),
                ('is_sent', models.NullBooleanField(default=False)),
                ('time_sent', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messaging.Message')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(blank=True, max_length=50, null=True)),
                ('notification_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Notification Type',
                'verbose_name_plural': 'Notification Types',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messaging.NotificationType'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]