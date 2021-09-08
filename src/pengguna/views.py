from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import  login_required
from django.contrib import auth, messages

from mainapp.models import JenjangPendidikan
from mainapp.utils import get_user_by_username
# Create your views here.

from pengguna.models import Pengguna


_DEBUG	     = 10
_INFO	     = 20
_SUCCESS     = 25
_WARNING	 = 30
_ERROR	     = 40


app_name = 'pengguna'

@login_required
def index(request):
    context = {}
    pengguna = Pengguna.objects.get(user=request.user)

    context['pengguna'] = pengguna

    html = app_name + '/index.html'
    return render (request, html, context) 

@login_required
def add(request):
    context = {}
    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +  '/add.html'
    return render (request, html,context) 

@login_required
def edit(request, id):
    context = {}

    context['obj'] = Pengguna.objects.get(id=id)
    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +  '/edit.html'
    return render (request, html,context)  


def impl_save_pengguna(request, data, _POST, tipe):

    data.nomor_induk_anggota = _POST.get('nomor_induk_anggota')
    data.nama_lengkap = _POST.get('nama_lengkap')
    data.nama_panggilan = _POST.get('nama_panggilan')
    data.jenis_kelamin = _POST.get('jenis_kelamin')
    data.tempat_lahir = _POST.get('tempat_lahir')
    data.tanggal_lahir = _POST.get('tanggal_lahir')
    ijazah_tertinggi = JenjangPendidikan.objects.get(pk= _POST.get('ijazah_tertinggi'))
    data.fk_ijazah_tertinggi = ijazah_tertinggi

    data.nomor_hp = _POST.get('nomor_hp')
    data.email = _POST.get('email')
    if (tipe == 'new'):
        data.user = get_user_by_username(_POST.get('username'))

    return data

@login_required
def save(request):
    func_name = "save"
    context = {}

    print("THIS IS SAVE FUNC @" + app_name) 
    if request.method == 'POST':
         
        _POST = request.POST


        if (_POST.get('pk')) :
            # means update
            pk = _POST.get('pk')
            try:
                data = Pengguna.objects.get(pk=_POST.get('pk'))
                data = impl_save_pengguna(request, data, _POST, 'update')
                data.save()

            except Exception as e:
                print ("exce on @" + app_name + "/" + func_name)
                print (e)

                msg = str(e)
                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('pengguna:edit', args=[pk]))    
        else:
            try:
                data = Pengguna()
                data = impl_save_pengguna(request, data, _POST, 'new')
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
    


@login_required
def delete(request, id):
    pass 