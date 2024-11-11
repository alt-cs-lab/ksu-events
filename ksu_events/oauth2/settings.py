# ksu_events/oauth2/settings.py
from django.conf import settings

# default social account providers configuration
SOCIALACCOUNT_PROVIDERS = {
    'MLH': {
        'APP': {
            'client_id': getattr(settings, 'MLH_CLIENT_ID', ''),
            'secret': getattr(settings, 'MLH_SECRET', ''),
            'key': ''
        },
        'SCOPE': ['email', 'phone_number', 'demographics', 'birthday', 'education']
    }
}

ACCOUNT_ADAPTER = 'ksu_events.oauth2.accountAdapter.CustomAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'ksu_events.oauth2.provider.MLHProvider'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
