# Generated by Django 4.1.1 on 2022-10-14 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_images_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='certificate',
        ),
    ]
