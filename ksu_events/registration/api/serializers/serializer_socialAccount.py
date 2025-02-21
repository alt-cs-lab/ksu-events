from rest_framework import serializers
from allauth.socialaccount.models import SocialAccount


class SocialAccountSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='registration:user-detail'
    )

    class Meta:
        model = SocialAccount
        fields = ('user', 'uid', 'extra_data')
        read_only_fields = fields
