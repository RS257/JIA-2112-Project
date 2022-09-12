from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]