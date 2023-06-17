from datetime import date
from django.db.models import OuterRef
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from store.models import Material, Product


@login_required(login_url='authentication:login_view')
def index(request):

    query_results = Material.objects.all()
    return render(
        request,
        'store/index.html',
        context={
            'query_results': query_results
        }
    )


@login_required(login_url='authentication:login_view')
def products(request):
    list_of_products = Product.objects.all()
    return render(
        request,
        'store/products.html',
        context={
            'list_of_products': list_of_products,

        }
    )


@login_required(login_url='authentication:login_view')
def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(
        request,
        'store/product_view.html',
        context={
            "product": product,
        }
    )


@login_required(login_url='store:fail')
def home(request):
    return render(request,
                  'store/home.html')


def fail(request):
    return render(request,
                  'store/fail.html')


@login_required(login_url='authentication:login_view')
def update_store(request):
    if request.method == 'POST':
        request_file = request.FILES[
            'order'] if 'order' in request.FILES else None
        if request_file:
            new_name = str(date.today())
            request_file.name = new_name
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
            uploaded_file_url = fs.url(file)

            return render(
                request,
                'store/update.html',
                context={
                    'uploaded_file_url': uploaded_file_url,
                }
            )
    return render(
        request,
        'store/update.html',
    )
