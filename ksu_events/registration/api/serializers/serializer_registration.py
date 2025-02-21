from rest_framework import serializers

from registration.api.serializers import UserSerializer
from registration.models import Registrations


# TODO: Rename and update to match the Registrations model
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='registration:user-detail'
    )

    hackathon = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='hackathon-detail'
    )

    class Meta:
        model = Registrations
        fields = (
            'user', 'all_ethnicities', 'year_in_school', 'updated_at', 'hackathon')
        read_only_fields = (
            'user', 'all_ethnicities', 'year_in_school', 'updated_at', 'hackathon')

# TODO: Rename and update to match the Registrations model
class UserProfileExpandedSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserSerializer(
        many=False,
        read_only=True
    )

    hackathon = serializers.SlugRelatedField(many=False, read_only=True, slug_field='hackathon')
    major = serializers.SlugRelatedField(many=True, read_only=True, slug_field='value')

    class Meta:
        model = Registrations
        fields = (
            'user', 'all_ethnicities', 'year_in_school',
            'updated_at', 'created_at', 'hackathon', 'cardID', 'major',
            'shirt_size', 'dietary_restrictions', 'mlh_communication',
            'country', 'shirt_size', "is_minor"
        )
        read_only_fields = fields

# TODO: Rename and update to match the Registrations model
class UserProfileShortSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(
        many=False,
        read_only=True
    )

    season = serializers.SlugRelatedField(many=False, read_only=True, slug_field='season')
    major = serializers.SlugRelatedField(many=True, read_only=True, slug_field='value')

    class Meta:
        model = Registrations
        fields = (
            'user', 'year_in_school', 'season', 'cardID', 'major',
            'shirt_size', 'dietary_restrictions', 'shirt_size'
        )
        read_only_fields = fields
