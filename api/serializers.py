from rest_framework import serializers
from archives.models import File, Data


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