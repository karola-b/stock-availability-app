from django.db import models


class Material(models.Model):
    material_id = models.CharField(max_length=50, primary_key=True)
    material_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=5, decimal_places=2)


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=100)


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE)
    material_id = models.ForeignKey(
        'Material', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
