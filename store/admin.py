from django.contrib import admin

from store.models import Material, Product, ProductMaterial, Color

admin.site.register(Material)

admin.site.register(Product)

admin.site.register(ProductMaterial)

admin.site.register(Color)
