from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product_view, name='product_view'),
    path('products/update', views.update_store, name='update'),
    path('home/', views.home, name='home'),
    path('fail/', views.fail, name='fail'),
]
