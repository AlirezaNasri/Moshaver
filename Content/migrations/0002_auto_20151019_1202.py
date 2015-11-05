# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.ManyToManyField(to='Content.ImageContent', null=True, blank=True),
            preserve_default=True,
        ),
    ]
