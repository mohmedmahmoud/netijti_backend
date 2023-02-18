from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
# Create your models here.




class Sector(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    number = models.CharField(max_length=10)
    
    name = models.CharField(max_length=50)
    score = models.DecimalField(
    max_digits=5, decimal_places=2,
    validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('20.00'))]
    )
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name+" "+self.score;


