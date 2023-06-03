from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from store.models import Material, Product, ProductMaterial


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


@login_required(login_url='authenticate:login')
def products(request):
    list_of_products = Product.objects.all()
    return render(
        request,
        'store/products.html',
        context={
            'list_of_products': list_of_products,

        }
    )


@login_required(login_url='authenticate:login')
def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(
        request,
        'store/product_view.html',
        context={
            "product": product,
        }
    )
