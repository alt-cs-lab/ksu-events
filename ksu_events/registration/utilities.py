from hackkstate.models import Hackathon
from registration.apps import RegistrationConfig
from registration.models import Registrations
from registration.models.model_users import User  # TODO: replace with the get_user django call


def get_auth_user_info(user: User):
    if user.is_authenticated:
        active_season = Hackathon.objects.get_active_season()
        profile = Registrations.objects.get_registration_hackation(user=user, hackathon_id=active_season)
        active_season = Registrations.objects.is_active(profile=profile, active_season=active_season)

        return {
            'auth': {'admin': user.is_staff or user.is_superuser,
                     'is_organizer': user.groups.filter(name='Organizers').exists(),
                     'email': user.email,
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'season': active_season,
                     'authenticated': True}}
    return {
        'auth': {'admin': False,
                 'season': False,
                 'authenticated': False}}
