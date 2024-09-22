from django.shortcuts import (
    render, 
    HttpResponse
)

def home(request):
    return HttpResponse("working just fine and dandy!")