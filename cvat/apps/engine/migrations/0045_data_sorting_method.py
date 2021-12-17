# Generated by Django 3.1.13 on 2021-12-03 08:06

import cvat.apps.engine.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0044_auto_20211123_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='sorting_method',
            field=models.CharField(choices=[('lexicographical', 'LEXICOGRAPHICAL'), ('natural', 'NATURAL'), ('predefined', 'PREDEFINED'), ('random', 'RANDOM')], default=cvat.apps.engine.models.SortingMethod['LEXICOGRAPHICAL'], max_length=15),
        ),
    ]