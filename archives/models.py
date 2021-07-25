from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class File(models.Model):
    name = models.TextField(max_length=50)
    date = models.DateTimeField()
    status = models.TextField(max_length=50, default="sin procesar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Data(models.Model):
    boro = models.TextField(max_length=50)
    objectid = models.IntegerField(default=0, unique=True)
    the_geom = models.TextField(max_length=250)
    type = models.TextField(max_length=50)
    provider = models.TextField(max_length=250)
    name = models.TextField(max_length=250)
    location = models.TextField(max_length=250)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    location_t = models.TextField(max_length=250)
    remarks = models.TextField(max_length=250)
    city = models.TextField(max_length=50)
    ssid = models.TextField(max_length=250)
    sourceid = models.TextField(max_length=250)
    activated = models.DateTimeField()
    borocode = models.IntegerField(default=0)
    boroname = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.ManyToManyField(File)

    def __str__(self):
        return self.title
