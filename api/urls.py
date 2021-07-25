from django.urls import path
from .views import UploadAPIView, FilesAPIView, DataAPIView 


urlpatterns = [
    path('upload', UploadAPIView.as_view()),
    path('files', FilesAPIView.as_view()),
    path('data', DataAPIView.as_view()),
]
