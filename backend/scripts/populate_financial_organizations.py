import pandas as pd

from django.db import transaction

from organizations.models import FinancialOrganization

def populate_financial_organizations():
    with transaction.atomic():
        file_path = "scripts/finOrgs.xlsx"
        df = pd.read_excel(file_path, dtype=str)
        df = df.where(pd.notnull(df), None) 
        for row in df.itertuples(index=False, name=None):
            name = row[0]
            _, _ = FinancialOrganization.objects.get_or_create(
                name=name,
                defaults={
                    'directors_board': row[2],
                    'management_board_chairman': row[3],
                    'management_board_members': row[4],
                    'chief_accountant': row[7],
                    'bin': row[8],
                    'address': row[9],
                    'phone_number': row[10].split(',')[0] if row[10] else None,
                    'email': row[11].split(',')[0] if row[11] else None,
                    'url': row[12],
                    'license': row[13]
                }
            )
