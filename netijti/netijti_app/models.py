# import datetime
# from django.utils import timezone
# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
# from decimal import Decimal
# # Create your models here.



# # Ce modèle stocke les informations sur les secteurs, les filieres  ...
# class Sector(models.Model):
#     name = models.CharField(max_length=50)
#     nameAr= models.CharField(max_length=50, null=True)
#     description = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name



# # Ce modèle stocke les informations sur les résultats
# class Result(models.Model):
#     number = models.CharField(max_length=10, primary_key=True)
#     name = models.CharField(max_length=50)
#     score = models.DecimalField(
#     max_digits=5, decimal_places=2,
#     validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('20.00'))]
#     )
#     # Le secteur associé au résultat.
#     sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # Des données supplémentaires associées au résultat, sous forme de dictionnaire.
#     metadata = models.JSONField(default=dict, null=True)
    
#     def __str__(self):
#         return f"{self.name} {str(self.score)}"
#     # def save(self, *args, **kwargs):
#     #     for key, value in self.metadata.items():
#     #         if isinstance(value, datetime.datetime):
#     #             self.metadata[key] = timezone.make_aware(value).isoformat()
#     #     super().save(*args, **kwargs)    

# # from django.test import TestCase
# # from decimal import Decimal
# # from models import Sector, Result

# # class SectorModelTest(TestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         Sector.objects.create(name='Test Sector')

# #     def test_sector_name(self):
# #         sector = Sector.objects.get(id=1)
# #         field_label = sector._meta.get_field('name').verbose_name
# #         self.assertEqual(field_label, 'name')

# #     def test_sector_name_max_length(self):
# #         sector = Sector.objects.get(id=1)
# #         max_length = sector._meta.get_field('name').max_length
# #         self.assertEqual(max_length, 50)

# # class ResultModelTest(TestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         sector = Sector.objects.create(name='Test Sector')
# #         Result.objects.create(number='001', name='Test Result', score=Decimal('10.50'), sector=sector)

# #     def test_result_name(self):
# #         result = Result.objects.get(number='001')
# #         expected_name = f"{result.name} {str(result.score)}"
# #         self.assertEqual(str(result), expected_name)

# #     def test_result_score_min_value(self):
# #         result = Result.objects.get(number='001')
# #         min_value = result._meta.get_field('score').validators[0].limit_value
# #         self.assertEqual(min_value, Decimal('0.00'))

# #     def test_result_score_max_value(self):
# #         result = Result.objects.get(number='001')
# #         max_value = result._meta.get_field('score').validators[1].limit_value
# #         self.assertEqual(max_value, Decimal('20.00'))

# #     def test_result_metadata_default(self):
# #         result = Result.objects.get(number='001')
# #         self.assertEqual(result.metadata, {})
