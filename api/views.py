from rest_framework import generics, views, response
from .serializers import FileSerializer
from archives.models import File, Data
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
#class FileAPIView(generics.ListAPIView):
#    queryset = File.objects.all()
#    serializer_class = FileSerializer


class FileUploadAPIView(views.APIView):
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
            destination = open(f'public/upload/{str(file_obj.id)}_{file_obj.name}', 'wb+')
            
            for chunk in file_ref.chunks():
                destination.write(chunk)
            destination.close()
            
            serializer = FileSerializer(file_obj)
            output = serializer.data 

        return JsonResponse(output, status = status)
        