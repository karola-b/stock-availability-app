import tabula as tb
import pandas as pd

from django.core.management import BaseCommand


class Command(BaseCommand):
   def handle(self, *args, **options):
      file_name = 'store/eksport_produktow_z_zamowien.pdf'
      df = tb.read_pdf(
         file_name, pages='all',
         area=(10, 10, 1000, 470),
         pandas_options={'header': None},
         lattice=True
      )[0]
      df.drop(columns=[1, 2, 3], inplace=True)
      df.columns = df.loc[0].values
      df.drop([0], axis=0, inplace=True)
      df['Jm'] = df['Jm'].str.replace('szt.', '')
      df.rename(columns={'Jm': 'amount', 'Kod towaru': 'code'}, inplace=True)
      df.to_csv('store/data.csv', index=False)

