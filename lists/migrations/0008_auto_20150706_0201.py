# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_list_item_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
    ]
