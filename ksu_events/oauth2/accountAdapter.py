from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
# from hackkstate.models import Hackathon
# from registration.models import Registrations

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        url = super().get_login_redirect_url(request)
        
        # if 'login/callback' in request.path:
            # active_season = Hackathon.objects.get_active_season()
            # profile = Registrations.objects.get_registration_hackathon(user=request.user, hackathon_id=active_season)
            # active_season = Registrations.objects.is_active(profile=profile, active_season=active_season)

            # if profile is None or not active_season:
                # url = reverse('registration:register')

        return url
