# Generated by Django 4.1.3 on 2022-12-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_user_date_of_birth_remove_user_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='User', max_length=30),
        ),
    ]
