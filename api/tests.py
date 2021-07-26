from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from archives.models import File, Data
from .serializers import FileSerializer

# Create your tests here.
class ApiTest(TestCase):
    
    def test_upload_api_view(self):
        self.client = APIClient()
        response = self.client.post('/api/upload')
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        

    def test_files_api_view(self):
        self.client = APIClient()
        response = self.client.get('/api/files')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)

    def test_data_api_view(self):
        self.client = APIClient()
        response = self.client.get('/api/data')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)

    def test_csv_api_view(self):
        self.client = APIClient()
        response = self.client.get('/api/csv')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)
    