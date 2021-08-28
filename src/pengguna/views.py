from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import  login_required
from django.contrib import auth, messages

from .models import Pengguna
from mainapp.utils import get_user_by_username
# Create your views here.


_DEBUG	     = 10
_INFO	     = 20
_SUCCESS     = 25
_WARNING	 = 30
_ERROR	     = 40


app_name = 'pengguna'

def index(request):
    context = {}
    member = Pengguna.objects.filter(user=request.user)
    context['penggunas'] = member.values()

    print(member)    

    html = 'pengguna/index.html'
    return render (request, html, context) 

def add(request):
    context = {}

    html = 'pengguna/add.html'
    return render (request, html,context) 

def edit(request):
    pass 

def save(request):
    func_name = "save"
    context = {}

    print("THIS IS SAVE FUNC @" + app_name) 
    if request.method == 'POST':
        _POST = request.POST
        try:
            data = Pengguna()
            data.nama_lengkap = _POST.get('nama_lengkap')
            data.nama_panggilan = _POST.get('nama_panggilan')
            data.tanggal_lahir = _POST.get('tanggal_lahir')
            data.user = get_user_by_username(_POST.get('username'))
            data.save()

        except Exception as e:
            print ("exce on @" + app_name + "/" + func_name)
            print (e)

            msg = str(e)
            messages.add_message(request, _ERROR, msg)
            return HttpResponseRedirect(reverse('pengguna:add'))

        msg = 'berhasil assign pengguna'
        messages.add_message(request, _SUCCESS, msg)
        return HttpResponseRedirect(reverse('pengguna:index'))
        
    return HttpResponseRedirect(reverse('pengguna:index'))
    


def delete(request, id):
    pass 