from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout


# Create your views here.
User = get_user_model()

def login_view(request):

    if request.method == 'GET':
        return render(request,
                  "authentication/login.html")

    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user=user)

        return redirect('store:home')

def logout_view(request):
    logout(request)
    return redirect('authentication:login_view')