from django.core.management.base import BaseCommand, CommandError
from ksu_events.registration.models import Registrations


class Command(BaseCommand):
    help = 'Sets all Card IDs of user profiles'

    def handle(self, *args, **options):
        count = 1
        for profile in Registrations.objects.all():
            profile.cardID = count
            profile.save()
            print(count)
            count += 1


