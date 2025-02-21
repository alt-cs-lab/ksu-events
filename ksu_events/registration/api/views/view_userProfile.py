from rest_framework import viewsets

# from hackkstate.api.mixins import MultipleFieldLookupMixin
from ksu_events.registration.api.serializers.serializer_registration import UserProfileSerializer, UserProfileExpandedSerializer
from ksu_events.registration.models.model_registrations import Registrations
from rest_framework.decorators import action
from rest_framework.response import Response


class UserProfileViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Registrations.objects.all().order_by('user')
    serializer_class = UserProfileSerializer
    filterset_fields = ['user', 'season']
    lookup_fields = ['user', 'season']
    search_fields = ['user']

    @action(methods=['get'], url_name='get_qr_code', url_path='get_qrcode', detail=False)
    def get_qr_code(self, request):
        user_profile = self.get_object()
        return Response(user_profile.get_qr_code())


class UserProfileViewSetExpanded(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Registrations.objects.all().order_by('user')
    serializer_class = UserProfileExpandedSerializer
    filterset_fields = ['user', 'season']
    search_fields = ['user']
