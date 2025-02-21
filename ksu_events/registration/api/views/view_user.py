from rest_framework import viewsets

from registration.api.serializers.serial_user import UserSerializer
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('last_name')
    serializer_class = UserSerializer
    filterset_fields = ['email']
