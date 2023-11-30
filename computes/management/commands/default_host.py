from django.core.management.base import BaseCommand, CommandError
from computes.models import Compute
from vrtManager.connection import CONN_SOCKET


class Command(BaseCommand):
    def handle(self, *args, **options):
        obj = Compute.objects.filter(hostname='localhost').first()
        if not obj:
            obj = Compute(name='local', hostname='localhost', details='The local service', type=CONN_SOCKET)
            obj.save()
            self.stdout.write('create new')
        else:
            self.stdout.write('created: ' + obj.name)
