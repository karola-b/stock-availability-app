from django.core.management import BaseCommand
import pandas as pd

from store.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.create()
        df = pd.read_csv('store/data_new.csv')
        for index, row in df.iterrows():
            product = Product.objects.filter(code=row['code'])
            if product:
                Order.products.add(product, through_defaults={'amount': row['amount']})
            else:
                print(f'Brak produktu o kodzie {row["code"]} (liczba {row["amount"]})')

