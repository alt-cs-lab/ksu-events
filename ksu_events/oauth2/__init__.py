# In __init__.py of your authentication app
from allauth.socialaccount.providers import registry
from provider import MLHProvider

registry.register(MLHProvider)
