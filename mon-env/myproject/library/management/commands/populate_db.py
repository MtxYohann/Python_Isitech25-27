from django.core.management.base import BaseCommand
from ...models import Author, Category, Book, Loan
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        # Supprimer les données existantes pour éviter les doublons
        Loan.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()

        # Créer des auteurs
        authors_data = [
            {'first_name': 'Victor', 'last_name': 'Hugo', 'nationality': 'Français', 'birth_date': '1802-02-26'},
            {'first_name': 'J.K.', 'last_name': 'Rowling', 'nationality': 'Britannique', 'birth_date': '1965-07-31'},
            {'first_name': 'George', 'last_name': 'Orwell', 'nationality': 'Britannique', 'birth_date': '1903-06-25'},
            {'first_name': 'Agatha', 'last_name': 'Christie', 'nationality': 'Britannique', 'birth_date': '1890-09-15'},
            {'first_name': 'Mark', 'last_name': 'Twain', 'nationality': 'Américain', 'birth_date': '1835-11-30'},
        ]
        authors = []
        for data in authors_data:
            author = Author.objects.create(**data)
            authors.append(author)
            self.stdout.write(f'Created author: {author}')

        # Créer des catégories
        categories_data = ['Fiction', 'Non-Fiction', 'Science-Fiction']
        categories = []
        for name in categories_data:
            category = Category.objects.create(name=name)
            categories.append(category)
            self.stdout.write(f'Created category: {category}')

        # Créer 20 livres
        books_data = [
            {'title': 'Les Misérables', 'isbn': '9780451419439', 'publication_year': 1862, 'stock_dispo': 5, 'stock_max': 10, 'description': 'Roman historique', 'language': 'Français', 'nb_pages': 1232, 'edition': 'Édition classique', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Cosette-sweeping-les-miserables-emile-bayard-1862.jpg/500px-Cosette-sweeping-les-miserables-emile-bayard-1862.jpg'},
            {'title': 'Harry Potter à l\'école des sorciers', 'isbn': '9780747532699', 'publication_year': 1997, 'stock_dispo': 3, 'stock_max': 8, 'description': 'Fantasy pour enfants', 'language': 'Français', 'nb_pages': 320, 'edition': '1ère édition', 'image_url': 'https://m.media-amazon.com/images/I/51dv0fAPslL._SY445_SX342_ML2_.jpg'},
            {'title': '1984', 'isbn': '9780451524935', 'publication_year': 1949, 'stock_dispo': 4, 'stock_max': 6, 'description': 'Dystopie', 'language': 'Français', 'nb_pages': 328, 'edition': 'Édition poche', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/1984JLH1.jpg/500px-1984JLH1.jpg'},
            {'title': 'Le Meurtre de Roger Ackroyd', 'isbn': '9780062073565', 'publication_year': 1926, 'stock_dispo': 2, 'stock_max': 5, 'description': 'Roman policier', 'language': 'Français', 'nb_pages': 256, 'edition': 'Édition collector', 'image_url': 'https://example.com/ackroyd.jpg'},
            {'title': 'Les Aventures de Tom Sawyer', 'isbn': '9780486400778', 'publication_year': 1876, 'stock_dispo': 6, 'stock_max': 12, 'description': 'Aventure jeunesse', 'language': 'Français', 'nb_pages': 274, 'edition': 'Édition scolaire', 'image_url': 'https://example.com/tom.jpg'},
            {'title': 'Notre-Dame de Paris', 'isbn': '9780140443530', 'publication_year': 1831, 'stock_dispo': 1, 'stock_max': 4, 'description': 'Roman historique', 'language': 'Français', 'nb_pages': 512, 'edition': 'Édition intégrale', 'image_url': 'https://example.com/notredame.jpg'},
            {'title': 'Harry Potter et la Chambre des Secrets', 'isbn': '9780439064873', 'publication_year': 1998, 'stock_dispo': 3, 'stock_max': 7, 'description': 'Fantasy', 'language': 'Français', 'nb_pages': 368, 'edition': '2ème édition', 'image_url': 'https://example.com/harry2.jpg'},
            {'title': 'La Ferme des Animaux', 'isbn': '9780451526342', 'publication_year': 1945, 'stock_dispo': 5, 'stock_max': 9, 'description': 'Satire politique', 'language': 'Français', 'nb_pages': 112, 'edition': 'Édition illustrée', 'image_url': 'https://example.com/animaux.jpg'},
            {'title': 'Le Crime de l\'Orient-Express', 'isbn': '9780062693662', 'publication_year': 1934, 'stock_dispo': 4, 'stock_max': 8, 'description': 'Roman policier', 'language': 'Français', 'nb_pages': 256, 'edition': 'Édition deluxe', 'image_url': 'https://example.com/orient.jpg'},
            {'title': 'Les Aventures de Huckleberry Finn', 'isbn': '9780486280615', 'publication_year': 1884, 'stock_dispo': 2, 'stock_max': 6, 'description': 'Aventure', 'language': 'Français', 'nb_pages': 320, 'edition': 'Édition moderne', 'image_url': 'https://example.com/huck.jpg'},
            {'title': 'Les Travailleurs de la Mer', 'isbn': '9782070404823', 'publication_year': 1866, 'stock_dispo': 3, 'stock_max': 7, 'description': 'Roman', 'language': 'Français', 'nb_pages': 480, 'edition': 'Édition critique', 'image_url': 'https://example.com/travailleurs.jpg'},
            {'title': 'Harry Potter et le Prisonnier d\'Azkaban', 'isbn': '9780439136365', 'publication_year': 1999, 'stock_dispo': 4, 'stock_max': 10, 'description': 'Fantasy', 'language': 'Français', 'nb_pages': 464, 'edition': '3ème édition', 'image_url': 'https://example.com/harry3.jpg'},
            {'title': 'La Révolte des Animaux', 'isbn': '9782070368224', 'publication_year': 1945, 'stock_dispo': 1, 'stock_max': 3, 'description': 'Satire', 'language': 'Français', 'nb_pages': 112, 'edition': 'Édition bilingue', 'image_url': 'https://example.com/revolte.jpg'},
            {'title': 'Mort sur le Nil', 'isbn': '9780062073558', 'publication_year': 1937, 'stock_dispo': 5, 'stock_max': 11, 'description': 'Policier', 'language': 'Français', 'nb_pages': 352, 'edition': 'Édition poche', 'image_url': 'https://example.com/nil.jpg'},
            {'title': 'Le Prince et le Pauvre', 'isbn': '9780486411101', 'publication_year': 1881, 'stock_dispo': 3, 'stock_max': 8, 'description': 'Aventure', 'language': 'Français', 'nb_pages': 256, 'edition': 'Édition jeunesse', 'image_url': 'https://example.com/prince.jpg'},
            {'title': 'L\'Homme Qui Rit', 'isbn': '9782070404830', 'publication_year': 1869, 'stock_dispo': 2, 'stock_max': 5, 'description': 'Roman', 'language': 'Français', 'nb_pages': 640, 'edition': 'Édition complète', 'image_url': 'https://example.com/homme.jpg'},
            {'title': 'Harry Potter et la Coupe de Feu', 'isbn': '9780439139601', 'publication_year': 2000, 'stock_dispo': 4, 'stock_max': 9, 'description': 'Fantasy', 'language': 'Français', 'nb_pages': 768, 'edition': '4ème édition', 'image_url': 'https://example.com/harry4.jpg'},
            {'title': 'Pourquoi pas les femmes ?', 'isbn': '9782070368231', 'publication_year': 1943, 'stock_dispo': 1, 'stock_max': 4, 'description': 'Essai', 'language': 'Français', 'nb_pages': 96, 'edition': 'Édition originale', 'image_url': 'https://example.com/femmes.jpg'},
            {'title': 'Le Mystère de la Chambre Jaune', 'isbn': '9782253004625', 'publication_year': 1907, 'stock_dispo': 3, 'stock_max': 7, 'description': 'Policier', 'language': 'Français', 'nb_pages': 288, 'edition': 'Édition mystère', 'image_url': 'https://example.com/chambre.jpg'},
            {'title': 'Un Yankee à la cour du roi Arthur', 'isbn': '9780486282114', 'publication_year': 1889, 'stock_dispo': 2, 'stock_max': 6, 'description': 'Humour', 'language': 'Français', 'nb_pages': 416, 'edition': 'Édition humoristique', 'image_url': 'https://example.com/yankee.jpg'},
        ]
        books = []
        for data in books_data:
            data['author'] = random.choice(authors)
            data['category'] = random.choice(categories)
            book = Book.objects.create(**data)
            books.append(book)
            self.stdout.write(f'Created book: {book.title}')

        # Créer quelques emprunts
        for _ in range(5):
            book = random.choice(books)
            if book.stock_dispo > 0:
                loan = Loan.objects.create(
                    book=book,
                    borrower_full_name='Test User',
                    borrower_email='test@example.com',
                    library_card_number='12345',
                    borrow_date=timezone.now(),
                    due_date=timezone.now() + timedelta(days=14),
                    status='borrowed'
                )
                book.stock_dispo -= 1
                book.save()
                self.stdout.write(f'Created loan for: {book.title}')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))