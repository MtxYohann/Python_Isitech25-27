from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def hello_library_view(request: HttpRequest) -> HttpResponse:
    """_summary_
    Args:
        request (HttpRequest): la requete entrante
    Returns:
        HttpResponse: la reponse HTTP avec le message "Hello, library!"
    """
    return HttpResponse("Hello, library!")

def library_list(request: HttpRequest) -> HttpResponse:
    """_summary_
    Args:
        request (HttpRequest): la requete entrante
    Returns:
        HttpResponse: la reponse HTTP avec le message "Library List!"
    """
    return HttpResponse("Library List!")