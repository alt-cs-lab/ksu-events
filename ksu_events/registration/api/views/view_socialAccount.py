from rest_framework import viewsets

from registration.api.serializers.serializer_socialAccount import SocialAccountSerializer
from allauth.socialaccount.models import SocialAccount


class SocialAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SocialAccount.objects.all().order_by('user')
    serializer_class = SocialAccountSerializer
    filterset_fields = ['user', 'uid']
    search_fields = ['extra_data']


