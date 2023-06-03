from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Material


@login_required(login_url='authenticate:login')
def index(request):

    query_results = Material.objects.all()
    return render(
        request,
        'store/index.html',
        context={
            'query_results': query_results
        }
    )

