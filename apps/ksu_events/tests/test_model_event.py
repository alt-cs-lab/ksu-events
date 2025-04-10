# Create your tests here.
from django.test import TestCase

from django.utils import timezone
from ksu_events.models import Event

class HackathonModelTest(TestCase):
	def setUp(self):
		self.event = Event.objects.create(
			name='Hackathon 2022',
			event_start_date=timezone.now(),
			event_end_date=timezone.now(),
			registration_start_date=timezone.now(),
			registration_end_date=timezone.now(),
			location='Virtual',
		)

	def test_str_representation(self):
		self.assertEqual(str(self.event), 'Hackathon 2022')