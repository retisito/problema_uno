from .serializers import FileSerializer, DataSerializer, CsvSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, views
from archives.models import File, Data
import mimetypes
#from django.views import generic

# Create your views here.

class UploadAPIView(views.APIView):
    def post(self, request, format = 'text/csv'):
        output = None
        status = 201
        
        try:
            file_ref = request.FILES['name']    
            file_obj = File.objects.create(name = file_ref.name, date = request.data['date'])        
        except Exception as e:
            msj = 'El cuerpo debe contener los parametros <name> archivo text/csv, <date> fecha YYYY-MM-DD'

            if e.__class__.__name__ == 'ValidationError':
                msj = 'El valor de <date> no debe ser vacio. El formato de <date> debe ser YYYY-MM-DD',

            output = { 'err': 'cuerpo mal formado', 'msj': msj}
            status = 400    
        else:    
            handler = open(f'public/upload/{str(file_obj.id)}_{file_obj.name}', 'wb+')
            
            for chunk in file_ref.chunks():
                handler.write(chunk)
            handler.close()
            
            serializer = FileSerializer(file_obj)
            output = serializer.data 

        return JsonResponse(output, status = status)
        

class FilesAPIView(generics.ListAPIView):
    queryset = File.objects.all().filter(status = 'sin procesar')
    serializer_class = FileSerializer


class DataAPIView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class CsvAPIView(generics.ListAPIView):
    queryset = File.objects.all().filter(status = 'procesado')
    serializer_class = CsvSerializer


class CsvDetailAPIView(views.APIView):
    def get(self, request, pk):
        try:
            file = File.objects.get(pk = pk)
        except Exception as e:
            output = {'err': 'file no existe', 'msj': 'El pk es invalido'}
            return JsonResponse(output, status = 400)
        else:
            path = f'public/processed/{str(file.id)}_{file.name}'

            handler = open(path, 'r')
            mime_type, _ = mimetypes.guess_type(path)    

            response = HttpResponse(handler, content_type = mime_type)
            response['Content-Disposition'] = "attachment; filename = %s" % file.name
            return response
          