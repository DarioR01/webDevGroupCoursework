# Generated by Django 4.1.3 on 2022-12-07 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_item_final_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='final_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 14, 10, 33, 11, 207621)),
        ),
    ]
