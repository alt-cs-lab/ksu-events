from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from ksu_events.oauth2.provider import MLHProvider

urlpatterns = default_urlpatterns(MLHProvider)