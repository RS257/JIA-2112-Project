# Generated by Django 4.1.1 on 2022-10-19 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_profile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
    ]
