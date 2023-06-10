from django.db import models


class Material(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)


class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    materials = models.ManyToManyField('Material', through='ProductMaterial')


class ProductMaterial(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE)
    material = models.ForeignKey(
        'Material', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)


class Color(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)


class Order(models.Model):
    products = models.ManyToManyField('Product', through='OrderProduct')
    created = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.SmallIntegerField()


# p1 = Product.objects.get(code='xyz')
#
# ProductMaterial.objects.filter(product=p1)
# p1.materials.all()


# class Material(models.Model):
#     material_id = models.CharField(max_length=50, primary_key=True)
#     material_name = models.CharField(max_length=100)
#     unit = models.CharField(max_length=10)
#     amount = models.DecimalField(max_digits=5, decimal_places=2)
#
#
# class Product(models.Model):
#     product_id = models.CharField(max_length=50, primary_key=True)
#     product_name = models.CharField(max_length=100)
#
#
# class ProductMaterial(models.Model):
#     product_id = models.ForeignKey(
#         'Product', on_delete=models.CASCADE)
#     material_id = models.ForeignKey(
#         'Material', on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=5, decimal_places=2)

