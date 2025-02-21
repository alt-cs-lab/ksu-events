from allauth.socialaccount.models import SocialAccount
from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxInput
from django.utils import timezone
from django.utils.safestring import mark_safe
from django_countries.widgets import CountrySelectWidget
from django.core.validators import EMPTY_VALUES

from ksu_events.models.model_events import Event
from ksu_events.registration.models.model_registrations import Registrations, age_by_date

# TODO: Update to match the Registrations model


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['shirt_size'].required = True
        self.fields['country'].required = True
        self.fields['country'].initial = "US"
        self.fields['shirt_size'].label = mark_safe ("Shirt Size.<sup>1</sup>")
        self.fields['is_minor'].label = mark_safe ("I am under 18 years old.<sup>2</sup>")
        # self.fields['is_coach'].label = mark_safe ("I am a coach/chaperone.<sup>3</sup>")
        age = self.age_helper()
        if age < 18:
            self.fields['is_minor'].initial = True

        self.fields['mlh_communication'].label = """I authorize MLH to send me an email where I can further opt into 
            the MLH Hacker, Events, or Organizer Newsletters and other communications from MLH."""

    class Meta:
        model = Registrations
        fields = (
            'ethnicity', 'country', 'year_in_school', 'shirt_size','dietary_restrictions',
            'mlh_communication', 'is_minor')
        widgets = {
            # 'qWhy': forms.Textarea(attrs={'rows': 4, 'cols': 60}),
            # 'qExpectations': forms.Textarea(attrs={'rows': 4, 'cols': 60}),
            # 'qPrize': forms.Textarea(attrs={'rows': 4, 'cols': 60}),
            'dietary_restrictions': forms.Textarea(attrs={'rows': 2, 'cols': 60}),
            'country': CountrySelectWidget(),
            'mlh_communication': CheckboxInput()
        }

    def age_helper(self):
        mlh = SocialAccount.objects.filter(user=self.request.user.id).first()
        if mlh is None:
            raise ValidationError("MLH data is missing, user must be authenticated through MLH.")
        season = Event.objects.get_active_season_query()
        if season is None:
            raise ValidationError("No active season. Please contact an administrator.")
        age = age_by_date(mlh.extra_data['date_of_birth'], season.Event_start_date)
        return age

    def clean(self):
        is_minor = self.cleaned_data.get('is_minor', False)
        # is_coach = self.cleaned_data.get('is_coach', False)
        # coach_email = self.cleaned_data.get('coach_email', False)
        # TODO: This age check is super hacky....parts should be done in the model...but things need to be refactored
        mlh = SocialAccount.objects.filter(user=self.request.user.id).first()
        if mlh is None:
            raise ValidationError("MLH data is missing, user must be authenticated through MLH.")
        season = Event.objects.get_active_season_query()
        if season is None:
            raise ValidationError("No active season. Please contact an administrator.")
        age = age_by_date(mlh.extra_data['date_of_birth'], season.Event_start_date)

        if age < 14:
            raise ValidationError('Users must be at least 14 years old to participate in Hack K-State')
        elif 14 <= age < 18:
            # if is_coach:
            #     self._errors['is_coach'] = self.error_class(["""Your birthdate indicates you are a minor.
            #                                                     Minors cannot be coaches."""])
            if not is_minor:
                self._errors['is_minor'] = self.error_class(['''Your birthdate indicates you are a minor. 
                                                                Please check the minor box.'''])
            # validate coach email
            # if coach_email in EMPTY_VALUES:
            #     self._errors['coach_email'] = self.error_class(['''A valid email of a your coach is required for minors.
            #                 A coach must be a teacher or administrator from your school (exceptions may be made on a
            #                 case-by-case basis on who can count as a coach).
            #                 Your coach must be registered before you can register.'''])
            # else:
            #     try:
            #         coach = Registrations.objects.get(user__email=coach_email)
            #     except Registrations.DoesNotExist:
            #         coach = None
            #     if coach is None or not coach.is_coach:
            #         self._errors['coach_email'] = self.error_class(['''A valid email of a your coach is required for
            #                 minors. The one given was not found or is not a coach.
            #                 A coach must be a teacher or administrator
            #                 from your school (exceptions may be made on a case-by-case basis
            #                 on who can count as a coach). Your coach must be registered before you can register.'''])
        else:  # is 18 or older
            if is_minor:
                raise ValidationError('Your birthdate indicates you are not a minor. Please uncheck the minor box.')

        return self.cleaned_data

    def save(self, user=None):
        user_profile = forms.ModelForm.save(self, commit=False)
        if user:
            # link the user to the profile
            user_profile.registration = user
        season = Event.objects.get_active_season_query()
        if season is None:
            raise Exception("No active season. Please contact an administrator.")
        user_profile.Event = season
        user_profile.created_at = timezone.now()
        user_profile.save()
        # save many to many relationship fields
        self.save_m2m()
        return user_profile
