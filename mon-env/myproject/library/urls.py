from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorDetailView

app_name = 'library'  # Namespace pour éviter les conflits

urlpatterns = [
    # Livres
    path('', views.book_list, name='book_list'),  # Liste de tous les livres avec pagination
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # Détail d'un livre spécifique (converter int pour pk)
    path('books/search/', views.book_search, name='book_search'),  # Recherche de livres
    path('categories/<int:pk>/books/', views.books_by_category, name='books_by_category'),  # Liste des livres par catégorie
    path('authors/<int:pk>/books/', views.books_by_author, name='books_by_author'),  # Liste des livres par auteur
    
    # Auteurs
    path('authors/', views.author_list, name='author_list'),  # Liste de tous les auteurs
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),  # Détail d'un auteur avec ses livres
    path('authors/search/', views.author_search, name='author_search'),  # Recherche d'auteurs
    
    # Emprunts
    path('loans/', views.loan_list_active, name='loan_list_active'),  # Liste des emprunts actifs
    path('loans/overdue/', views.loan_list_overdue, name='loan_list_overdue'),  # Liste des emprunts en retard
    path('loans/history/', views.loan_history, name='loan_history'),  # Historique des emprunts d'un usager (formulaire pour email)
    path('books/<int:book_id>/loan/', views.loan_create, name='loan_create'),  # Formulaire de création d'emprunt
    path('loans/<int:loan_id>/return/', views.loan_return, name='loan_return'),  # Formulaire de retour de livre
    
    # Pages statiques
    path('about/', views.about, name='about'),  # Page "À propos"
    path('contact/', views.contact, name='contact'),  # Page de contact
    path('books/class/', BookListView.as_view(), name='book_list_class'),
    path('books/<int:pk>/class/', BookDetailView.as_view(), name='book_detail_class'),
    path('authors/<int:pk>/class/', AuthorDetailView.as_view(), name='author_detail_class'),
    path('books/<int:book_id>/loan/class/', views.LoanCreateView.as_view(), name='loan_create_class'),
]