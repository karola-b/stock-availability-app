from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Material, Product


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


def products(request):
    list_of_products = Product.objects.all()
    return render(
        request,
        'store/products.html',
        context={
            'list_of_products': list_of_products
        }
    )
