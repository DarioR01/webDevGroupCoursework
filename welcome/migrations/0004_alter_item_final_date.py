# Generated by Django 4.1.3 on 2022-12-16 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_alter_item_final_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='final_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 13, 7, 5, 730259)),
        ),
    ]
