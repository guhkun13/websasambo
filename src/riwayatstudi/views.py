from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import  login_required
from django.contrib import auth, messages


from .models import RiwayatStudi
from mainapp.models import  JenjangPendidikan
from mainapp.utils import get_pengguna_or_none
# Create your views here.

_DEBUG	     = 10
_INFO	     = 20
_SUCCESS     = 25
_WARNING	 = 30
_ERROR	     = 40


app_name = 'riwayatstudi'
def index(request):
    context = {}
    
    pengguna = get_pengguna_or_none(request)
    datas = RiwayatStudi.objects.filter(fk_anggota=pengguna)
    context['datas'] = datas.values()

    print(datas)

    html = app_name + '/index.html'
    return render (request, html, context) 

@login_required
def add(request):
    context = {}

    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +'/add.html'
    return render (request, html,context) 


def edit(request, id):
    context = {}

    context['obj'] = RiwayatStudi.objects.get(id=id)
    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +  '/edit.html'
    return render (request, html,context)  

def save(request):
    func_name = "save"
    context = {}

    print("THIS IS SAVE FUNC @" + app_name) 
    if request.method == 'POST':         
        _POST = request.POST
        if (_POST.get('pk')) :
            # means update
            try:
                data = Pengguna.objects.get(pk=_POST.get('pk'))
                data.jenis_kelamin = _POST.get('jenis_kelamin')
                data.save()
            except Exception as e:
                print ("exce on @" + app_name + "/" + func_name)
                print (e)

                msg = str(e)
                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('pengguna:edit'))    
        else:
            # create new
            pengguna = get_pengguna_or_none(request)
            print(pengguna)
            try:
                data = RiwayatStudi()
                data.fk_anggota = pengguna
                data.nama_instansi = _POST.get('nama_instansi')
                data.nomor_induk_studi = _POST.get('nomor_induk_studi')
                data.negara = _POST.get('negara')

                tempprov = _POST.get('provinsi').split('|')

                data.id_provinsi = tempprov[0]
                data.nama_provinsi = tempprov[1]

                tempkab = _POST.get('kabupaten').split('|')
                data.id_kabupaten = tempkab[0]
                data.nama_kabupaten = tempkab[1]                
                

                temp_jenjang_pendidikan = _POST.get('jenjang_pendidikan')
                id_jenjang_pendidikan = temp_jenjang_pendidikan.split('|')[0]
                jenjang_pendidikan = JenjangPendidikan.objects.get(pk=id_jenjang_pendidikan)
                data.fk_jenjang_pendidikan = jenjang_pendidikan
                data.negara = _POST.get('negara')

                data.save()

            except Exception as e:
                print ("exce on @" + app_name + "/" + func_name)
                print (e)

                msg = str(e)
                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('riwayatstudi:add'))

            msg = 'berhasil assign pengguna'
            messages.add_message(request, _SUCCESS, msg)
            return HttpResponseRedirect(reverse('riwayatstudi:index'))
    
        
    return HttpResponseRedirect(reverse('riwayatstudi:index')) 

def delete(request, id):
    pass 