AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
]

CAS_SERVER_URL = 'https://signin.k-state.edu/WebISO/'
CAS_LOGOUT_COMPLETELY = True
CAS_REDIRECT_URL = '/'
