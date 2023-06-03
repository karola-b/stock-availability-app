from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# widok na magazyn
def index(request):
    return render(
        request,
        'store/index.html'
    )

@login_required(login_url='store:fail')
def home(request):
    return render(request,
                  'store/home.html')


def fail(request):
    return render(request,
                  'store/fail.html')

