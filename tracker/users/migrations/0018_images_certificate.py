# Generated by Django 4.1.1 on 2022-10-15 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_images_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='certificate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.certificate'),
        ),
    ]
