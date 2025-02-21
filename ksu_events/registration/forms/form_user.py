from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ksu_events.registration.models.model_users import User


# not used?
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields
