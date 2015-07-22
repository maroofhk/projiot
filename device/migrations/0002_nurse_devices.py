# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='devices',
            field=models.ManyToManyField(to='device.Device', blank=True),
            preserve_default=True,
        ),
    ]
