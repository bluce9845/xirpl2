from django.db import models

# Create your models here.
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('kelas/static/uploads/', filename)

class AboutStudent(models.Model):
    name = models.CharField(max_length=255)
    motto = models.CharField(max_length=255)
    studentImg = models.ImageField(upload_to=filepath, null=True, blank=False)
    about = models.CharField(max_length=600, null=True)
    hobi = models.CharField(max_length=255, null=True)
    skils = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Galery(models.Model):
    namaKegiatan = models.CharField(max_length=200)
    desKegiatan = models.CharField(max_length=300)
    imgKegiatan = models.ImageField(upload_to=filepath, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.namaKegiatan
