# Generated by Django 4.1.2 on 2022-12-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
