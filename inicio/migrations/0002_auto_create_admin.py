from django.db import migrations
from django.core.management import call_command

def create_admin(apps, schema_editor):
    call_command('ensure_admin')

class Migration(migrations.Migration):
    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin, migrations.RunPython.noop),
    ]