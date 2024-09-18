from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import AboutStudent
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    cards = AboutStudent.objects.all()
    paginator = Paginator(cards, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

@login_required(login_url="users:login")
def detail(request, id):
    detail_siswa = AboutStudent.objects.get(id=id)
    template = loader.get_template('detail_siswa.html')
    context = {
        'detail_siswa': detail_siswa
    }

    return HttpResponse(template.render(context, request))
