from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import environ

User = get_user_model()
env = environ.Env(  
    DEBUG=(bool, False)  
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        email = env("ADMIN_EMAIL", default='admin@example.com')
        new_password = env("ADMIN_PASSWORD", default='admin@123')
        try:
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write("No superusers found, creating one")
                User.objects.create_superuser(email=email, password=new_password)
                self.stdout.write("=======================")
                self.stdout.write("A superuser has been created")
                self.stdout.write(f"Email: {email}")
                self.stdout.write(f"Password: {new_password}")

                self.stdout.write("=======================")
            else:
                self.stdout.write("A superuser exists in the database. Skipping.")
        except Exception as e:
            self.stderr.write(f"There was an error {e}")
