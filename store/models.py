from django.db import models


class Material(models.Model):
    material_id = models.CharField(max_length=50, primary_key=True)
    material_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=100)


class ProductMaterial(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE)
    material_id = models.ForeignKey(
        'Material', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)


class Color(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

# p1 = Product.objects.get(code='xyz')
#
# ProductMaterial.objects.filter(product=p1)
# p1.materials.all()
