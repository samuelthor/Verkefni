# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20150908_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='title_text',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
