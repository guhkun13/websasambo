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
    return render (request, html, context)  

def impl_save(request, data, _POST):
    func_name = "impl_save"
    print ("#"+func_name)
    # create new
    pengguna = get_pengguna_or_none(request)
    print(pengguna.nama_lengkap)

    data.fk_anggota = pengguna
    data.nama_instansi = _POST.get('nama_instansi')
    data.nomor_induk_studi = _POST.get('nomor_induk_studi')
    data.negara = _POST.get('negara', 'INDONESIA')           
    
    is_indo = False
    if _POST.get('negara') == 'INDONESIA':
        is_indo = True

    data.is_indonesia = is_indo
   
    if not is_indo:
        data.id_provinsi = ''
        data.nama_provinsi = ''
        data.id_kabupaten = ''
        data.nama_kabupaten = ''
    else:
        tempprov = _POST.get('provinsi').split('|')
        print("tempprov = ", tempprov)

        data.id_provinsi = tempprov[0]
        data.nama_provinsi = tempprov[1]

        tempkab = _POST.get('kabupaten').split('|')
        print("tempkab = ", tempkab)

        data.id_kabupaten = tempkab[0]
        data.nama_kabupaten = tempkab[1]                
        
    data.alamat_kampus_luar_negeri = _POST.get('alamat_kampus_luar_negeri')
    
    temp_jenjang_pendidikan = _POST.get('jenjang_pendidikan')
    id_jenjang_pendidikan = temp_jenjang_pendidikan.split('|')[0]
    print("id_jenjang_pendidikan = ", id_jenjang_pendidikan)
    jenjang_pendidikan = JenjangPendidikan.objects.get(pk=id_jenjang_pendidikan)
    data.fk_jenjang_pendidikan = jenjang_pendidikan

    data.fakultas = _POST.get('fakultas')
    data.jurusan = _POST.get('jurusan')
    data.jalur_masuk = _POST.get('jalur_masuk')
    data.tahun_masuk = _POST.get('jalur_masuk')
    data.tahun_keluar = _POST.get('jalur_masuk')
    data.alasan_keluar = _POST.get('jalur_masuk')
    
    data.is_beasiswa = _POST.get('jalur_masuk')
    data.nama_beasiswa = _POST.get('jalur_masuk')

    data.save()

def save(request):
    func_name = "save"
    context = {}

    print("@" + app_name + " func #" + func_name) 
    if request.method == 'POST':         
        _POST = request.POST
        print(_POST)
        if (_POST.get('pk')) :
            print("UPDATe!!!")
            # means update
            try:
                data = RiwayatStudi.objects.get(pk=_POST.get('pk'))
                impl_save(request, data, _POST)                
            except Exception as e:
                print ("EX on @" + app_name + "#" + func_name)
                print (e)

                msg = str(e)
                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('riwayatstudi:edit',args=[_POST.get('pk')]))                        
        else:            
            print("CREATe NEW!!!")
            try:
                data = RiwayatStudi()
                impl_save(request, data, _POST)
            except Exception as e:
                print ("EX on @" + app_name + "#" + func_name)
                print (e)

                msg = str(e)
                messages.add_message(request, _ERROR, msg)
                return HttpResponseRedirect(reverse('riwayatstudi:add'))

            msg = 'berhasil tambah ' + app_name
            messages.add_message(request, _SUCCESS, msg)
            return HttpResponseRedirect(reverse('riwayatstudi:index'))
    
        
    return HttpResponseRedirect(reverse('riwayatstudi:index')) 

def delete(request, id):
    func_name = 'delete'
    try:
        data = RiwayatStudi.objects.get(pk=id)
        data.delete()
    except Exception as e:
        print ("exce on @" + app_name + "/" + func_name)
        print (e)

        msg = str(e)
        messages.add_message(request, _ERROR, msg)
    return HttpResponseRedirect(reverse('riwayatstudi:index'))    