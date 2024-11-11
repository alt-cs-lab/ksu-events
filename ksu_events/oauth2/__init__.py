from allauth.socialaccount.providers import registry
from ksu_events.oauth2.provider import MLHProvider

registry.register(MLHProvider)
