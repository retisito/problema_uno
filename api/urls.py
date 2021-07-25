from django.urls import path
from .views import UploadAPIView, FilesAPIView, DataAPIView, CsvAPIView, CsvDetailAPIView


urlpatterns = [
    path('upload', UploadAPIView.as_view()),
    path('files', FilesAPIView.as_view()),
    path('data', DataAPIView.as_view()),
    path('csv', CsvAPIView.as_view()),
    path('csv/<int:pk>', CsvDetailAPIView.as_view()),
]
