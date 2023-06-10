import tabula as tb
import pandas as pd

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
       file = 'store/eksport_produktow_z_zamowien.pdf'
       df = tb.read_pdf(
          file, pages='all', area=(10, 10, 1000, 470),
          pandas_options={'header': None}, lattice=True)[0]

       df2 = df.drop(df.columns[[-1, 1, 2, 3]], axis=1, inplace=True)
       df.columns = df.loc[0].values
       df = df.tail(-1)
       df['Jm'] = df['Jm'].str.replace('szt.', '')
       df.rename(columns={'Jm': 'amount', 'Kod towaru': 'code'}, inplace=True)

       df.to_csv('store/data.csv', index=False)
