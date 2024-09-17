from django.contrib import admin
from .models import AboutStudent, Galery

# Register your models here.
class aboutStudent(admin.ModelAdmin):
  list_display = ("name", "motto")

admin.site.register(AboutStudent, aboutStudent)

class galery(admin.ModelAdmin):
    list_display = ("namaKegiatan", "added")
    
admin.site.register(Galery, galery) 