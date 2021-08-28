import json
from pprint import pprint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout, get_user
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User

from mainapp.models import * 
from mainapp.utils import * 
from .utils import * 

def index(request):
    html = 'survey/index.html'

    context = {}
    context['app'] = 'survey'
    context['data'] = 'data'

    # record_log(True, request.user.username, "open " + context['app'] + " index")

    return render(request, html, context)    

def riwayat_studi_add(request):
    context = {}
    html = 'survey/riwayat_studi/add_or_edit.html'

    try:
        obj_pengguna = Pengguna.objects.get(user=request.user)
    except Exception as e:
        obj_pengguna = None
    
    provinsis = DaftarProvinsi.objects.all()
    kabupatens = DaftarKabupaten.objects.all()
    jenjang_pendidikans = JenjangPendidikan.objects.all()

    context['provinsis'] = provinsis
    context['kabupatens'] = kabupatens
    context['jenjang_pendidikans'] = jenjang_pendidikans

    context['pengguna'] = obj_pengguna
    context['app'] = 'survey'
    context['data'] = 'data'

    # record_log(True, request.user.username, "open " + context['app'] + " index")

    return render(request, html, context)    

def riwayat_studi_create_or_update(request):
    context = {}

    if request.method == "POST":
        print(request.POST)
        _POST = request.POST
        rwstudi = RiwayatStudi()
        rwstudi.fk_anggota = get_pengguna_or_none(request)
        rwstudi.nama_instansi = _POST.get('nama_instansi')
        rwstudi.nomor_induk_studi = _POST.get('nomor_induk_studi')
        rwstudi.negara = _POST.get('negara')
        rwstudi.fk_provinsi = get_obj_provinsi(_POST.get('provinsi'))
        rwstudi.fk_kabupaten = get_obj_kabupaten(_POST.get('kabupaten'))
        rwstudi.fk_jenjang_pendidikan = get_obj_jenjang_pendidikan(_POST.get('jenjang_pendidikan'))        
        rwstudi.fakultas = _POST.get('fakultas')
        rwstudi.jurusan = _POST.get('jurusan')
        rwstudi.tahun_masuk = _POST.get('tahun_masuk')
        rwstudi.jalur_masuk = _POST.get('jalur_masuk')
        rwstudi.tahun_keluar = _POST.get('tahun_keluar') or None
        rwstudi.alasan_keluar = _POST.get('alasan_keluar')
        rwstudi.is_beasiswa = _POST.get('is_beasiswa')
        rwstudi.save()

    context['app'] = 'survey'
    context['data'] = 'data'
    
    return HttpResponseRedirect(reverse('mainapp:index'))


