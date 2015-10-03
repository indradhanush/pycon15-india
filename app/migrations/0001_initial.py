# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=uuid.uuid4, max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]
