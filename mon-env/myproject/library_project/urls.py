from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# Vue simple pour la page d'accueil (redirige vers la liste des livres)
def home(request):
    return redirect('library:book_list')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'), 
    path('library/', include('library.urls', namespace='library')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 