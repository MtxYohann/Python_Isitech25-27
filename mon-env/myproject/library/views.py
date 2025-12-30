from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Category,Loan
from .forms import LoanForm 

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})

def loan_create(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        form.instance.book = book  # Définit le livre sur l'instance du formulaire avant validation
        if form.is_valid():
            loan = form.save()  # Sauvegarde directement, car book est déjà défini
            # Diminue le nombre d'exemplaires disponibles
            if book.stock_dispo > 0:
                book.stock_dispo -= 1
                book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = LoanForm()
    return render(request, 'library/loan_form.html', {'form': form, 'book': book})