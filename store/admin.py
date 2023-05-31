from django.contrib import admin

from store.models import Material, Product, ProductMaterial

admin.site.register(Material)

admin.site.register(Product)

admin.site.register(ProductMaterial)