from rest_framework import serializers
from archives.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'name', 'date', 'status', 'created_at', 'updated_at')