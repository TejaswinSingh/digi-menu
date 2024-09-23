from django.shortcuts import (
    HttpResponse,
)

def home(request):
    return HttpResponse("working just fine and dandy!")