from django.urls import path
from django_cas_ng import views as cas_views

urlpatterns = [
    path('login/', cas_views.LoginView.as_view(), name='cas_ng_login'),
    path('logout/', cas_views.LogoutView.as_view(), name='cas_ng_logout'),
]