from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea el superusuario admin con contraseña 1234 si no existe'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', '1234')
            self.stdout.write(self.style.SUCCESS('Superusuario "admin" creado con contraseña "1234"'))
        else:
            u = User.objects.get(username='admin')
            u.set_password('1234')
            u.save()
            self.stdout.write(self.style.SUCCESS('Superusuario "admin" actualizado con contraseña "1234"'))