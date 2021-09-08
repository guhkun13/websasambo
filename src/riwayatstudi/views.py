from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import  login_required
from django.contrib import auth, messages


from mainapp.models import  JenjangPendidikan
from mainapp.utils import get_pengguna_or_none

from riwayatstudi.models import RiwayatStudi
from riwayatstudi.utils import impl_save

_DEBUG	     = 10
_INFO	     = 20
_SUCCESS     = 25
_WARNING	 = 30
_ERROR	     = 40

app_name = 'riwayatstudi'

@login_required
def index(request):
    context = {}
    
    pengguna = get_pengguna_or_none(request)
    datas = RiwayatStudi.objects.filter(fk_anggota=pengguna)
    context['datas'] = datas

    print(datas)

    html = app_name + '/index.html'
    return render (request, html, context) 

@login_required
def add(request):
    print ("before render in ADD")
    print(request)
    print(request.GET)
    print(request.POST)
    context = {}

    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +'/add.html'
    
    return render (request, html,context) 

@login_required
def edit(request, id):
    context = {}

    context['obj'] = RiwayatStudi.objects.get(id=id)
    context['jenjang_pendidikans'] = JenjangPendidikan.objects.all()

    html = app_name +  '/edit.html'

    
    return render (request, html, context)  


@login_required
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

@login_required
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