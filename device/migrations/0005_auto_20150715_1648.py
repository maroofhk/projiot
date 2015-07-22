# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20150715_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='active',
            field=models.BooleanField(max_length=5),
            preserve_default=True,
        ),
    ]
