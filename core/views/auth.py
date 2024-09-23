from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from google.oauth2 import id_token
from google.auth.transport import requests
import environ
from django.shortcuts import (
    render, 
    HttpResponse,
    redirect
)
env = environ.Env(  
    DEBUG=(bool, False)  
)
User = get_user_model()


def sign_in(request):
    """
    allows user to sign-in using their Google account
    """
    return render(request, "core/sign-in.html")

def sign_out(request):
    """
    logs the user out and redirects them to sign-in page
    """
    logout(request)
    return redirect('core:sign-in')

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    We get the user-details (email, profile pic etc) from Google and create/fetch 
    the corresponding User object in our database. Finally, we log the user in.
    """
    if request.method != "POST":
        return HttpResponse("<h1>Method not allowed.</h1>", status=405)

    token = request.POST.get('credential', None)

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), env("GOOGLE_OAUTH_CLIENT_ID") 
        )
    except ValueError:
        return HttpResponse("<h1>You're not authorised to access this page.</h1>", status=403)

    try:
        user = User.objects.get(email=user_data["email"])
    except User.DoesNotExist:
        user = User.objects.create_user(email=user_data["email"])
        user.first_name = user_data["name"]
        user.picture = user_data["picture"]
        user.save()

    login(request, user)

    return redirect('core:sign-in')