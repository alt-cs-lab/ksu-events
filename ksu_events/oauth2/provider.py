from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.base import ProviderAccount, AuthAction
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class MLHAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('html_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_url')

    def to_str(self):
        dflt = super(MLHAccount, self).to_str()
        return next(
            value
            for value in (
                self.account.extra_data.get('name', None),
                self.account.extra_data.get('login', None),
                dflt
            )
            if value is not None
        )


class MLHProvider(OAuth2Provider):
    id = 'MLH'
    name = 'Major League Hacking'
    account_class = MLHAccount

    def get_auth_url(self, request, action):
        if action == AuthAction.REAUTHENTICATE:
            url = 'https://my.mlh.io/oauth/authorize'
        else:
            url = 'https://my.mlh.io/oauth/token'
        return url

    def get_default_scope(self):
        # return []
        scope = ['email', 'phone_number', 'demographics', 'birthday', 'education']
        return scope

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'))


provider_classes = [MLHProvider]
