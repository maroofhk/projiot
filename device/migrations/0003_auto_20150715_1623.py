# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_nurse_devices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='active',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
