# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('messname', models.CharField(max_length=500)),
                ('messenger', models.CharField(max_length=500)),
                ('race', models.CharField(max_length=500)),
                ('messabout', models.CharField(max_length=2000)),
                ('money', models.CharField(max_length=2000)),
                ('messtest', models.CharField(max_length=1000)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
