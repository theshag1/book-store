from django.urls import path
from book.views import *

urlpatterns = {
    path('', HomeView.as_view(), name='homepage'),
    path('korzinka/', BuyBook.as_view(), name='Buy')
}
