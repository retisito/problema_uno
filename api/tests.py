from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from scripts.data_load import run as data_load_run
from scripts.create_csv import run as create_csv_run


# Create your tests here.
class ApiTest(TestCase):
    
    def test_workflow_api_view(self):
        self.client = APIClient()
        
        # Haciendo un POST <api/upload> con cuerpo mal formado
        response = self.client.post('/api/upload')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Haciendo un POST <api/upload> con data valida
        with open('public/test/sample.csv') as file_csv:
            response = self.client.post('/api/upload', {'name': file_csv, 'date': '2021-07-21'})
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        # Haciendo un GET <api/files> sin haber procesado el file sample.csv. Se espear 1 entrada
        response = self.client.get('/api/files')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 1)
    
        # Haciendo un GET <api/data> sin haber procesado el file sample.csv. Se espear 0 entrada
        response = self.client.get('/api/data')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)

        # Cargando la data del file de pruebas
        data_load_run()

        # Haciendo un GET <api/files> con el file sample.csv en proceso. Se espera 0 entradas
        response = self.client.get('/api/files')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)

        # Haciendo un GET <api/data> con el file sample.csv en proceso. Se espear 4 entrada
        response = self.client.get('/api/data')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 4)

        # Haciendo un GET <api/csv> con el file sample.csv en proceso. Se espera 0 entradas
        response = self.client.get('/api/csv')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 0)

        # Creando CSV a partir de la data almacenada
        create_csv_run()

        # Haciendo un GET <api/csv> con el file sample.csv procesado. Se espera 0 entradas
        response = self.client.get('/api/csv')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 1)

    def test_file_api_view(self):
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
    