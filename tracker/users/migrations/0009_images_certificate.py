# Generated by Django 4.1.1 on 2022-10-13 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_images_image_name_alter_images_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='certificate',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.certificate'),
        ),
    ]
