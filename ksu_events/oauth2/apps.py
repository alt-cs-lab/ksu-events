from django.apps import AppConfig
from django.conf import settings

class OAuth2Config(AppConfig):
    name = 'ksu_events.oauth2'
    label = 'ksu_events_oauth2'

    def ready(self):
        from allauth.socialaccount.providers import registry
        from ksu_events.oauth2.provider import MLHProvider
        registry.register(MLHProvider)
        # Override the default settings with package defaults if not provided by the consumer
        default_settings = {
            'SOCIALACCOUNT_PROVIDERS': {
                'mlh': {
                    'APP': {
                        'client_id': getattr(settings, 'MLH_CLIENT_ID', ''),
                        'secret': getattr(settings, 'MLH_SECRET', ''),
                        'key': ''
                    },
                    'SCOPE': ['email', 'phone_number', 'demographics', 'birthday', 'education']
                }
            },
            'ACCOUNT_ADAPTER': 'ksu_events.oauth2.accountAdapter.CustomAccountAdapter',
            'SOCIALACCOUNT_ADAPTER': 'ksu_events.oauth2.provider.MLHProvider',
            # Add more defaults as needed
        }

        for setting, value in default_settings.items():
            if not hasattr(settings, setting):
                setattr(settings, setting, value)
