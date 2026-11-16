
from django.core.management.base import BaseCommand
from call.models import Persona


class Command(BaseCommand):
    help = 'Comando de carga'
    def handle(self, *args, **options):
        persona = Persona(nombre="Fran",primer_apellido="Grande",segundo_apellido="Franco")
        persona.save()