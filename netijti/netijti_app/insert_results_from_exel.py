import openpyxl
from models import Result, Sector

# Ouvrir le fichier Excel
workbook = openpyxl.load_workbook('file.xlsx')
worksheet = workbook.active

# Récupérer les données de chaque ligne et les insérer dans la base de données
for row in worksheet.iter_rows(min_row=2, values_only=True):
    sector = Sector.objects.get(name='Bac 2022')
    result = Result(
        name=row[0],
        number=row[1],
        score=row[2],
        sector=sector,
        metadata=row
    )
    result.save()

print("end insert data")
