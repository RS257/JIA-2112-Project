# Generated by Django 4.1.1 on 2022-11-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='limited',
            field=models.BooleanField(default=True, verbose_name='Limited'),
        ),
    ]
