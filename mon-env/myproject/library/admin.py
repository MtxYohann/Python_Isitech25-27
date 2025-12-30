from django.contrib import admin
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Book, Author, Loan, Category

# Personnalisation du site admin
admin.site.site_header = "Administration Bibliothèque Numérique"
admin.site.site_title = "Bibliothèque Admin"
admin.site.index_title = "Bienvenue dans l'admin de la bibliothèque"

# Inline pour visualiser les emprunts actifs dans Book
class LoanInline(admin.TabularInline):
    model = Loan
    extra = 0
    readonly_fields = ('borrow_date', 'due_date', 'status')
    can_delete = False
    show_change_link = True

# Admin pour Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'stock_dispo', 'stock_max')
    list_filter = ('category', 'author', 'publication_year', 'language')
    search_fields = ('title', 'isbn', 'author__first_name', 'author__last_name')
    readonly_fields = ('catalogued_date',)
    fieldsets = (
        ('Informations Générales', {
            'fields': ('title', 'isbn', 'publication_year', 'author', 'category')
        }),
        ('Stock et Détails', {
            'fields': ('stock_dispo', 'stock_max', 'description', 'language', 'nb_pages', 'edition', 'image_url')
        }),
        ('Métadonnées', {
            'fields': ('catalogued_date',),
            'classes': ('collapse',)
        }),
    )
    inlines = [LoanInline]
    
    actions = ['mark_unavailable']
    
    def mark_unavailable(self, request, queryset):
        queryset.update(stock_dispo=0)
        self.message_user(request, "Les livres sélectionnés ont été marqués comme indisponibles.")
    mark_unavailable.short_description = "Marquer comme indisponibles"

    def save_model(self, request, obj, form, change):
        if obj.stock_dispo > obj.stock_max:
            raise ValidationError("Le stock disponible ne peut pas dépasser le stock maximum.")
        super().save_model(request, obj, form, change)

# Inline pour visualiser les livres dans Author
class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    readonly_fields = ('isbn', 'publication_year')
    can_delete = False
    show_change_link = True

# Admin pour Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'nationality', 'birth_date', 'date_of_death')
    list_filter = ('nationality',)
    search_fields = ('first_name', 'last_name')
    inlines = [BookInline]
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Nom Complet"

# Admin pour Loan
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower_full_name', 'borrow_date', 'status', 'penalty')
    list_filter = ('status', 'borrow_date', 'due_date')
    search_fields = ('borrower_full_name', 'borrower_email', 'library_card_number', 'book__title')
    readonly_fields = ('borrow_date', 'return_date')
    actions = ['mark_returned']
    
    def mark_returned(self, request, queryset):
        for loan in queryset.filter(status='borrowed'):
            loan.return_date = timezone.now()
            loan.status = 'returned'
            loan.book.stock_dispo += 1
            loan.book.save()
            loan.save()
        self.message_user(request, "Les emprunts sélectionnés ont été marqués comme retournés et le stock mis à jour.")
    mark_returned.short_description = "Marquer comme retourné"
    
    def penalty(self, obj):
        return obj.calculate_penalty()
    penalty.short_description = "Pénalité (€)"

    def save_model(self, request, obj, form, change):
        if obj.status == 'returned' and not obj.return_date:
            obj.return_date = timezone.now()
        if obj.return_date and obj.return_date > obj.due_date:
            obj.status = 'overdue'
        super().save_model(request, obj, form, change)

# Admin pour Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'book_count')
    search_fields = ('name', 'description')
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = "Nombre de Livres"