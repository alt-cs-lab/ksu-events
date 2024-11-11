from allauth.account.views import LoginView as AllauthLoginView, LogoutView as AllauthLogoutView

class LoginView(AllauthLoginView):
    template_name = 'oauth/login.html'

class LogoutView(AllauthLogoutView):
    template_name = 'oauth/logout.html'

oauth2_login = LoginView.as_view()
oauth2_callback = LogoutView.as_view()
