# Generated by Django 4.1.1 on 2022-10-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_images_options_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
