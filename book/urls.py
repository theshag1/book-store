from django.urls import path
from book.views import *

urlpatterns = [
    path('',Enterview.as_view(), name='Enter'),
    path('home/', BookListView.as_view(), name='homepage'),
    # path('home/<str>', Login_not.as_view(), name='dont_login'),
    path('books/<int:pk>', BookDetilView.as_view(), name='book_detial')
]
