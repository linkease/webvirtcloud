from django.core.management.base import BaseCommand, CommandError
from computes.models import Compute
from vrtManager.connection import CONN_SOCKET
from appsettings.models import AppSettings


class Command(BaseCommand):
    def handle(self, *args, **options):
        obj = Compute.objects.filter(hostname='localhost').first()
        if not obj:
            obj = Compute(name='local', hostname='localhost', details='The local service', type=CONN_SOCKET)
            obj.save()
            self.stdout.write('create new')
        else:
            self.stdout.write('created: ' + obj.name)

        obj = AppSettings.objects.get(pk=35)
        if obj and obj.value == 'default':
            obj.value = 'virtio'
            obj.save()
