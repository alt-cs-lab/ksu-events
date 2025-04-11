from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your app routes
    path('', include('ksu_events.events.urls')), # Main app...replace '' with /events if you want to use the events prefix instead of making this the default
    path('registration/', include('ksu_events.registration.urls')),
    # Optional: if using Django allauth
    # path('accounts/', include('allauth.urls')),
]
