# Generated by Django 4.1.1 on 2022-10-19 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_images_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='uploaded_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 19, 20, 31, 58, 112248), null=True, verbose_name='Uploaded on'),
        ),
    ]
