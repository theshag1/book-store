from django.contrib.auth.views import LoginView


class Accountlogin(LoginView):
    template_name = 'accounts/login.html'
    success_url = 'accounts/profile'


class NotFoundAccount(LoginView):
    template_name = 'accounts/dont_account.html'
