from django.shortcuts import render

from .models import RiwayatStudi
from mainapp.utils import get_pengguna_or_none
# Create your views here.


app_name = 'riwayatstudi'
def index(request):
    context = {}
    
    member = get_pengguna_or_none(request)
    datas = RiwayatStudi.objects.filter(fk_anggota=member)
    context['datas'] = datas.values()

    print(datas)
    
    html = app_name + '/index.html'
    return render (request, html, context) 

def add(request):
    context = {}

    html = app_name +'/add.html'
    return render (request, html,context) 


def edit(request):
    pass 

def save(request):
    pass 

def delete(request, id):
    pass 