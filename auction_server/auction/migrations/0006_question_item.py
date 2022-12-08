# Generated by Django 4.1.3 on 2022-12-08 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_remove_item_final_date_remove_item_question_id_array_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_set', to='auction.item'),
            preserve_default=False,
        ),
    ]
