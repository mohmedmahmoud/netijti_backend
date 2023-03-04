from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Sector, Result
from .serializers import ResultSerializer


class SectorTestCase(TestCase):
    
    def setUp(self):
        Sector.objects.create(name="Test Sector", nameAr="Test Sector Arabic", description="Test Sector Description")
        
    def test_sector_name(self):
        sector = Sector.objects.get(name="Test Sector")
        self.assertEqual(sector.name, "Test Sector")
        
    def test_sector_nameAr(self):
        sector = Sector.objects.get(name="Test Sector")
        self.assertEqual(sector.nameAr, "Test Sector Arabic")
        
    def test_sector_description(self):
        sector = Sector.objects.get(name="Test Sector")
        self.assertEqual(sector.description, "Test Sector Description")
        
    def test_sector_str(self):
        sector = Sector.objects.get(name="Test Sector")
        self.assertEqual(str(sector), "Test Sector")



class ResultViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sector = Sector.objects.create(name='Sector 1', nameAr='القطاع 1', description='Description 1')
        self.result = Result.objects.create(number='110011', name='Result 1', score='10.50', sector=self.sector)
    
    def test_list_results(self):
        response = self.client.get(reverse('result-list'))
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True) 
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_result(self):
        response = self.client.get(reverse('result-detail', args=[self.result.number]))
        result = Result.objects.get(number=self.result.number)
        serializer = ResultSerializer(result)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_result(self):
        sector = Sector.objects.create(name='Sector 1', nameAr='القطاع 1', description='Description 1', id=2)
        
        data = {
            'number': '2',
            'name': 'Result 2',
            'score': '15.25',
            'sector': sector.pk,
            'metadata': {
                'key1': 'value1',
                'key2': 'value2'
            }
        }
        
        response = self.client.post(reverse('result-list'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Result.objects.count(), 2)
        self.assertEqual(Result.objects.get(number=data['number']).name, data['name'])
    
    # def test_update_result(self):
    #     data = {
    #         'name': 'Result 1 updated',
    #         'score': '12.75',
    #         'sector': self.sector.id,
    #         'metadata': {
    #             'key3': 'value3',
    #             'key4': 'value4'
    #         }
    #     }
    #     response = self.client.put(reverse('result-detail', args=[self.result.number]), data=data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Result.objects.count(), 1)
    #     self.assertEqual(Result.objects.get(number=self.result.number).name, data['name'])
    
    # def test_delete_result(self):
    #     response = self.client.delete(reverse('result-detail', args=[self.result.number]))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Result.objects.count(), 0)

