from django.db import migrations

def create_or_fix_admin(apps, schema_editor):
    from django.contrib.auth.models import User
    # This checks if the user exists; if not, it creates them. 
    # If they do exist, it forces them to be an admin with this password.
    user, created = User.objects.get_or_create(username='master_admin')
    user.set_password('ComplexPass123!')
    user.is_staff = True
    user.is_superuser = True
    user.save()

class Migration(migrations.Migration):
    dependencies = [
        # This must match the name of the LAST file in your migrations folder
        # Look in your migrations folder and replace '0001_initial' if there is a later number
        ('expenses', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_or_fix_admin),
    ]