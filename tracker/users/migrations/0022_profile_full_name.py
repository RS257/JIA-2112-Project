# Generated by Django 4.1.1 on 2022-10-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_certificate_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Full Name'),
        ),
    ]