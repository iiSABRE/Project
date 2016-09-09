# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordproject', '0006_wordrecord_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blob', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SoundPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordproject.Sound')),
            ],
        ),
        migrations.CreateModel(
            name='WordPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='wordrecord',
            name='englishWord',
        ),
        migrations.RemoveField(
            model_name='wordrecord',
            name='maoriWord',
        ),
        migrations.RemoveField(
            model_name='wordrecord',
            name='month',
        ),
        migrations.RemoveField(
            model_name='wordrecord',
            name='year',
        ),
        migrations.AddField(
            model_name='wordrecord',
            name='language',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wordrecord',
            name='word',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='wordpair',
            name='original',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original', to='wordproject.WordRecord'),
        ),
        migrations.AddField(
            model_name='wordpair',
            name='translation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordproject.WordRecord'),
        ),
        migrations.AddField(
            model_name='soundpair',
            name='wordpair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordproject.WordPair'),
        ),
    ]
