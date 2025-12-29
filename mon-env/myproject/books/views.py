from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def hello_todos_view(request: HttpRequest) -> HttpResponse:
    """_summary_
    Args:
        request (HttpRequest): la requete entrante
    Returns:
        HttpResponse: la reponse HTTP avec le message "Hello, todos!"
    """
    return HttpResponse("Hello, todos!")