# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20150715_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='active',
            field=models.TextField(max_length=5),
            preserve_default=True,
        ),
    ]
