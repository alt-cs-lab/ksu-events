# Create your tests here.
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from base.models import Event

class HackathonModelTest(TestCase):
	def setUp(self):
		self.event = Event.objects.create(
			name='Hackathon 2022',
			season='Spring',
			hackathon_start_date=timezone.now(),
			hackathon_end_date=timezone.now(),
			registration_start_date=timezone.now(),
			registration_end_date=timezone.now(),
			location='Virtual',
			status='upcoming'
		)

	def test_str_representation(self):
		self.assertEqual(str(self.hackathon), 'Hackathon 2022')

	def test_active_hackathon_validation(self):
		# Create another active hackathon
		Event.objects.create(
			name='Active Hackathon',
			season='Fall',
			mlh_app_id=2,
			hackathon_start_date=timezone.now(),
			hackathon_end_date=timezone.now(),
			registration_start_date=timezone.now(),
			registration_end_date=timezone.now(),
			location='Virtual',
			status='active'
		)

		# Try to save the current hackathon as active, should raise ValidationError
		with self.assertRaises(ValidationError):
			self.hackathon.save()

	def test_get_active_season(self):
		# Create an active hackathon
		active_event = Event.objects.create(
			name='Active Hackathon',
			season='Fall',
			mlh_app_id=2,
			hackathon_start_date=timezone.now(),
			hackathon_end_date=timezone.now(),
			registration_start_date=timezone.now(),
			registration_end_date=timezone.now(),
			location='Virtual',
			status='active'
		)

		# Get the active season
		active_season = Event.objects.get_active_season()

		self.assertEqual(active_season, 'Fall')

	def test_get_active_season_query(self):
		# Create an active hackathon
		active_event = Event.objects.create(
			name='Active Hackathon',
			season='Fall',
			mlh_app_id=2,
			hackathon_start_date=timezone.now(),
			hackathon_end_date=timezone.now(),
			registration_start_date=timezone.now(),
			registration_end_date=timezone.now(),
			location='Virtual',
			status='active'
		)

		# Get the active season query
		active_season_query = Event.objects.get_active_season_query()

		self.assertEqual(active_season_query.count(), 1)
		self.assertEqual(active_season_query.first(), active_event)