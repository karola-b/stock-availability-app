from django.core.management import BaseCommand
import pandas as pd

from store.models import Product, Order, ProductMaterial


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.create()
        df = pd.read_csv('store/data.csv')
        for index, row in df.iterrows():
            product = Product.objects.filter(code=row['code'])
            if product:
                product = product.first()
                order.products.add(
                    product,
                    through_defaults={
                        'amount': row['amount']
                    }
                )

                materials = product.materials.all()

                for material in materials:
                    amount = ProductMaterial.objects.get(
                        product=product,
                        material=material
                    ).amount
                    material.amount -= amount
                    material.save()
            else:
                print(
                    f'Brak produktu o kodzie {row["code"]} (liczba {row["amount"]})')