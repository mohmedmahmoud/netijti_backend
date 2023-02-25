
import datetime
import openpyxl
from netijti_app.models import Result, Sector

# Ouvrir le fichier Excel
workbook = openpyxl.load_workbook('static/res-proba-2022-2.xlsx', read_only=True)
worksheet = workbook.active

# Récupérer les données de chaque ligne et les insérer dans la base de données
for row in worksheet.iter_rows(min_row=2, values_only=True):
    sector = Sector.objects.get(name='Bac 2023')
    result = Result(
        name=row[3],
        number=row[1],
        score=row[6],
        sector=sector,
        metadata=row,
        created_at=datetime.datetime.now()  
    )
    result.save()

print("end insert data")
