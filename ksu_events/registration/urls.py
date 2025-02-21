from django.urls import path, include
from ksu_events.registration import views
from .api.router import router

urlpatterns = [
    # path('api/', include((router.urls, 'registration'))),
    path('api/', include(router.urls)),
    path('', views.RegistrationView.as_view(), name='register'),
    path('completed', views.CompletionPageView.as_view(), name='completed'),
]