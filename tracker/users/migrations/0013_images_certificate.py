# Generated by Django 4.1.1 on 2022-10-14 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_roles_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='certificate',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.certificate'),
        ),
    ]