# Generated by Django 4.1.2 on 2022-12-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0004_alter_item_final_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='final_date',
            field=models.DateTimeField(),
        ),
    ]