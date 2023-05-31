from django.shortcuts import render

from store.models import Material


def index(request):
    query_results = Material.objects.all()
    return render(
        request,
        'store/index.html',
        context={
            'query_results': query_results
        }
    )
