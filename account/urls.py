from django.urls import path
from account.views import *

urlpatterns = [
    path('login/', Accountlogin.as_view(), name='login'),
    path('login/<str>', NotFoundAccount.as_view(), name='dont_account')
]
