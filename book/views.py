from django.views.generic import ListView

from book.models import Book


class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "books"


class BuyBook(ListView):
    queryset = Book.objects.filter(id=3)
    template_name = 'polls/buy.html'
    context_object_name = "books"


