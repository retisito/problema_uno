from django.urls import path
from .views import FileUploadAPIView #FileAPIView, 


urlpatterns = [
    path('upload', FileUploadAPIView.as_view()),
    #path('', FileAPIView.as_view()),
]
