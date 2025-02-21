from django.utils import timezone

from django.urls import reverse
from django.shortcuts import redirect

from hackkstate.models import Hackathon
from hackkstate.util.common import get_hackathon_date_range, date_range_with_suffix
from hackkstate.util.mixins import CommonContextMixin
from hackkstate.views import HomePageView
from registration.forms.form_registration import RegistrationForm
from registration.models import Registrations
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from django.core.mail import send_mail

from registration.apps import RegistrationConfig

from django.views.generic import TemplateView, FormView

from registration.utilities import get_auth_user_info


class SecretPageView(LoginRequiredMixin, CommonContextMixin, TemplateView):
    template_name = "secret.html"
    page_name = "secret"
    data = "nadda"
    title = "Shhhh"

    # login_url = '/accounts/login'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(SecretPageView, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'activePage': self.page_name, 'data': str(self.request.user)})
        return context


# need to figure out how to convert this to an UpdateView
class RegistrationView(LoginRequiredMixin, CommonContextMixin, FormView):
    template_name = "registration.html"
    page_name = "Registration"
    title = "Registration"
    form_class = RegistrationForm

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def dispatch(self, request, *args, **kwargs):
        current_time = timezone.now()
        active_season = Hackathon.objects.get_active_season_query()
        registration_open = active_season.registration_start_date <= current_time <= active_season.registration_end_date
        if request.user.is_authenticated and registration_open:
            return super().dispatch(request, *args, **kwargs)
        elif registration_open and not request.user.is_authenticated:
            return redirect('account_login')
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'activePage': self.page_name})
        context.update(get_auth_user_info(self.request.user))
        return context

    def form_valid(self, form):
        form.save(self.request.user)
        tempUser = get_auth_user_info(self.request.user)
        season = tempUser['auth']['season']
        hackdates = date_range_with_suffix(season.hackathon_start_date, season.hackathon_end_date)
        # send auto-generated e-mail here
        send_mail(
            f"Hack K-State {season.hackathon} Registration Confirmation",
            f""" Hello {tempUser['auth']['first_name']}, \n
            Thank you for registering for Hack K-State for {hackdates}! Keep an eye on emails from the Hack K-State 
            organizing team. As the event gets closer, we will send out another email with information such as 
            day-of-event details, discord information, how to access free APIs, tools, resources, and the necessary 
            forms to fill out prior to attending.\n\n If you have any questions, please feel free to e-mail 
            hackkstate@ksu.edu to get in touch with our team.\n\n Thank you!\n\n Your Hack K-State Organizing Team""",
            f"{settings.EMAIL_FROM_NAME} <{settings.DEFAULT_FROM_EMAIL}>",
            [tempUser['auth']['email']]
        )
        return super().form_valid(form)

    def get_success_url(self):
        # this fills in the redirect URL on success
        # messages.add_message(self.request, messages.INFO, 'Registration was successful!')
        return reverse('registration:completed')


class CompletionPageView(LoginRequiredMixin, CommonContextMixin, TemplateView):
    template_name = "registration_completed.html"
    page_name = "Registration Completed"
    title = "Registered!"

    # login_url = '/accounts/login'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(CompletionPageView, self).get_context_data(**kwargs)

        active_season = Hackathon.objects.get_active_season()
        profile = Registrations.objects.get_registration_hackation(user=self.request.user, hackathon_id=active_season)
        active_season = Registrations.objects.is_active(profile=profile, active_season=active_season)

        context.update(
            {'title': self.title, 'activePage': self.page_name, 'name': "{} {}".format(self.request.user.first_name,
                                                                                       self.request.user.last_name),
             'season': active_season,
             })

        context.update(get_auth_user_info(self.request.user))
        return context
