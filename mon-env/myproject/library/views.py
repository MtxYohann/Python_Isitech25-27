from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from .models import Book, Author, Category, Loan
from .forms import LoanForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Vues de liste avec pagination et filtres
def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q', '')
    if query:
        books = books.filter(Q(title__icontains=query) | Q(isbn__icontains=query) | Q(author__first_name__icontains=query) | Q(author__last_name__icontains=query))
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/book_list.html', {'page_obj': page_obj, 'query': query})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def loan_list_active(request):
    loans = Loan.objects.filter(status='borrowed')
    return render(request, 'library/loan_list_active.html', {'loans': loans})

def loan_list_overdue(request):
    loans = Loan.objects.filter(status='overdue')
    return render(request, 'library/loan_list_overdue.html', {'loans': loans})

# Vues de détail avec affichage conditionnel
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    available = book.stock_dispo > 0
    return render(request, 'library/book_detail.html', {'book': book, 'available': available})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})

# Vues de formulaires avec validation et messages
def loan_create(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        form.instance.book = book
        if form.is_valid():
            loan = form.save()
            if book.stock_dispo > 0:
                book.stock_dispo -= 1
                book.save()
                messages.success(request, f"Emprunt de '{book.title}' réussi !")
            else:
                messages.error(request, "Aucun exemplaire disponible.")
                return redirect('library:book_detail', pk=book.pk)
            return redirect('library:book_detail', pk=book.pk)
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = LoanForm()
    return render(request, 'library/loan_form.html', {'form': form, 'book': book})

def loan_return(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    if loan.status != 'borrowed':
        messages.warning(request, "Cet emprunt n'est pas actif.")
        return redirect('library:book_detail', pk=loan.book.pk)
    if request.method == 'POST':
        loan.return_date = timezone.now()
        loan.status = 'returned'
        loan.book.stock_dispo += 1
        loan.book.save()
        loan.save()
        messages.success(request, f"Retour de '{loan.book.title}' confirmé.")
        return redirect('library:book_detail', pk=loan.book.pk)
    return render(request, 'library/loan_return_confirm.html', {'loan': loan})

# Autres vues fonctionnelles
def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(isbn__icontains=query) | Q(author__first_name__icontains=query) | Q(author__last_name__icontains=query)
    ) if query else Book.objects.none()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/book_search.html', {'page_obj': page_obj, 'query': query})

def books_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = category.books.all()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/books_by_category.html', {'category': category, 'page_obj': page_obj})

def books_by_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/books_by_author.html', {'author': author, 'page_obj': page_obj})

def author_search(request):
    query = request.GET.get('q', '')
    authors = Author.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(nationality__icontains=query)
    ) if query else Author.objects.none()
    return render(request, 'library/author_search.html', {'authors': authors, 'query': query})

def loan_history(request):
    email = request.GET.get('email', '')
    loans = Loan.objects.filter(borrower_email=email) if email else Loan.objects.none()
    return render(request, 'library/loan_history.html', {'loans': loans, 'email': email})

def about(request):
    return render(request, 'library/about.html')

def contact(request):
    return render(request, 'library/contact.html')



class BookListView(ListView):
    model = Book
    template_name = 'library/book_list_class.html'
    paginate_by = 10
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(isbn__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail_class.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available'] = self.object.stock_dispo > 0
        return context

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail_class.html'

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'library/loan_form_class.html'
    success_url = reverse_lazy('library:book_list')

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_id'])
        form.instance.book = book
        if book.stock_dispo > 0:
            book.stock_dispo -= 1
            book.save()
            messages.success(self.request, f"Emprunt réussi pour '{book.title}'.")
        else:
            messages.error(self.request, "Stock insuffisant.")
            return self.form_invalid(form)
        return super().form_valid(form)