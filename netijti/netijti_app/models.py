from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
# Create your models here.



# Ce modèle stocke les informations sur les secteurs, les filieres  ...
class Sector(models.Model):
    name = models.CharField(max_length=50)
    nameAr= models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# Ce modèle stocke les informations sur les résultats
class Result(models.Model):
    number = models.CharField(max_length=10)
    
    name = models.CharField(max_length=50)
    score = models.DecimalField(
    max_digits=5, decimal_places=2,
    validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('20.00'))]
    )
    # Le secteur associé au résultat.
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Des données supplémentaires associées au résultat, sous forme de dictionnaire.
    metadata = models.JSONField(default=dict, null=True)
    
    def __str__(self):
        return f"{self.name} {str(self.score)}"


