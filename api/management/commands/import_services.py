from django.core.management.base import BaseCommand, CommandError
from api.models import Service
import docker


class Command(BaseCommand):
    help = 'Import all currently running Services'

    def add_argument(self, parser):
        parser.add_arguments('service_id', nagrs="+", type=int)

    def handle(self, *args, **options):
        try:
            client = docker.from_env()
            images = client.images.list()
            import pdb; pdb.set_trace()
            # export
            pass
        except:
            raise CommandError("Error")

        self.stdou.write("self.style.SUCCESS('Successfully imprted")
