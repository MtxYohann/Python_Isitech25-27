from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1450),
            MaxValueValidator(datetime.date.today().year)
        ]
    )
    author = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='books')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    stock_dispo = models.IntegerField(validators=[MinValueValidator(0)])
    stock_max = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    language = models.CharField(max_length=50) 
    nb_pages = models.IntegerField(validators=[MinValueValidator(1)])
    edition = models.CharField(max_length=100)
    image_url = models.URLField()
    catalogued_date = models.DateField(auto_now_add=True)

    def clean(self):
        if self.stock_dispo > self.stock_max:
            raise ValidationError("Le nombre d'exemplaires disponibles ne peut pas dépasser le total.")
        super().clean()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50)
    biography = models.TextField()
    photo_url = models.URLField()
    website_url = models.URLField()

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Loan(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Emprunté'),
        ('returned', 'Retourné'),
        ('overdue', 'En retard'),
    ]

    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='loans')
    borrower_full_name = models.CharField(max_length=200)
    borrower_email = models.EmailField()
    library_card_number = models.CharField(max_length=20)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')
    librarian_comments = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.borrow_date.date() + datetime.timedelta(days=14)  
        super().save(*args, **kwargs)

    def is_overdue(self):
        return self.status == 'borrowed' and datetime.date.today() > self.due_date

    def calculate_penalty(self):
        if self.return_date and self.return_date.date() > self.due_date:
            days_late = (self.return_date.date() - self.due_date).days
            return days_late * 0.5  
        return 0

    def clean(self):
        if self.book.stock_dispo <= 0:
            raise ValidationError("Aucun exemplaire disponible pour cet emprunt.")
        
        active_loans = Loan.objects.filter(library_card_number=self.library_card_number, status='borrowed').exclude(pk=self.pk).count()
        if active_loans >= 5:
            raise ValidationError("Maximum 5 emprunts simultanés autorisés.")
        
        super().clean()

    def __str__(self):
        return f"Emprunt de {self.book.title} par {self.borrower_full_name}"
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_url = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name