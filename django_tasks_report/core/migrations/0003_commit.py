# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160904_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Task')),
                ('url', models.URLField(max_length=255, verbose_name='Url')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Repository', verbose_name='Repository')),
            ],
            bases=('core.task',),
        ),
    ]
