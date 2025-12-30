from django.contrib import admin
from .models import Book, Author, Loan, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'stock_dispo', 'stock_max')
    list_filter = ('category', 'language')
    search_fields = ('title', 'isbn')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'nationality')
    search_fields = ('first_name', 'last_name')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('borrower_full_name', 'book', 'borrow_date', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('borrower_full_name', 'book__title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)