from django.http import request
from rest_framework import serializers
from archives.models import File, Data

from django.utils.timezone import now

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id', 'name', 'date', #'status', 
            'created_at', 'updated_at'
        )


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = (
            'id', 'boro', 'objectid', 'the_geom',
            'type', 'provider', 'name', 'location', 
            'lat', 'lon', 'x', 'y', 'location_t',
            'remarks', 'city', 'ssid', 'sourceid', 
            'activated', 'borocode', 'boroname', 
            'created_at', 'updated_at'
        )


class CsvSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id', 'name', 'date', 'download_url', 
            'created_at', 'updated_at'
        )
    
    def get_download_url(self, file):
        request = self.context['request']
        return  f'{request.get_host()}/api/csv/{str(file.id)}'
