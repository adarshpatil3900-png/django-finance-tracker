from django.db import migrations

def create_or_fix_admin(apps, schema_editor):
    # This 'apps.get_model' is the safest way to get the User model inside a migration
    from django.contrib.auth.models import User
    
    try:
        # Check if the user exists
        user = User.objects.get(username='master_admin')
        user.set_password('ComplexPass123!')
        user.is_staff = True
        user.is_superuser = True
        user.save()
    except User.DoesNotExist:
        # If not, create them
        User.objects.create_superuser(
            username='master_admin',
            email='admin@example.com',
            password='ComplexPass123!'
        )

class Migration(migrations.Migration):
    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_or_fix_admin),
    ]