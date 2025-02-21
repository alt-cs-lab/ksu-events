from rest_framework import routers
from ksu_events.registration.api.views import UserProfileViewSet, UserProfileViewSetExpanded, UserViewSet, SocialAccountViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userProfiles', UserProfileViewSet, basename='userprofile') #TODO: added basename, needs tested
router.register(r'userProfilesExpanded', UserProfileViewSetExpanded, basename='userprofile_expanded') #TODO: added basename, needs tested
router.register(r'mlhInfo', SocialAccountViewSet)
# print(router.urls)