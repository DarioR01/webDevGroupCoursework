# Generated by Django 4.1.3 on 2022-12-02 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='./uploads')),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]