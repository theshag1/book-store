from django.views.generic import ListView, DetailView, TemplateView

from book.models import Book


class Enterview(TemplateView):
    template_name = 'enter.html'


class BookListView(ListView):
    queryset = Book.objects.order_by('-id')
    template_name = "home.html"
    context_object_name = "books"


class BookDetilView(DetailView):
    queryset = Book.objects.all()
    template_name = "books/book_detil.html"
    context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     book_id = self.kwargs.get(self.pk_url_kwarg)
    #     context['first_book'] = Book.objects.first()
    #     context['book'] = Book.objects.filter(id=book_id).first()
    #     return context
