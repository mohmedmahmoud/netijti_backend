# Parse the JSON data
import json


from bac_result_json import json_data
from models import Result, Sector






data = json.loads(json_data)

# Create a new Result instance for each object in the JSON array
sector = Sector.objects.get(name='Bac 2022')
for obj in data:
    result = Result(
        
        name=obj["NOM COMPLET"],
        number=obj["NODOSS"],
        score=obj["MOY-PROBATOIRE"],
        sector= sector,
        metadata=obj
    )
    result.save()
print("end insert data")