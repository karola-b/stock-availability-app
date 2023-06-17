import pandas as pd
import tabula as tb

from store.models import Product, Order, ProductMaterial


def fetch_from_csv(*args, **options):
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
                print(material.amount)
                print(type(material.amount))
                print(amount)
                print(type(amount))
                material.amount -= amount
                material.save()
        else:
            print(
                f'Brak produktu o kodzie {row["code"]} (liczba {row["amount"]})')

import os

def pdf_to_csv(file_name, *args, **options):
    file_path = os.path.join('orders', file_name)
    print(file_path)
    df = tb.read_pdf(
        file_path, pages='all',
        area=(10, 10, 1000, 470),
        pandas_options={'header': None},
        lattice=True)[0]
    df.drop(columns=[1, 2, 3], inplace=True)
    df.columns = df.loc[0].values
    df.drop([0], axis=0, inplace=True)
    df['Jm'] = df['Jm'].str.replace('szt.', '')
    df.rename(columns={'Jm': 'amount', 'Kod towaru': 'code'}, inplace=True)
    df.to_csv('store/data.csv', index=False)

