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

from .utils import *
# from .forms import *

from django.views.generic import DetailView, View

# ajax class
# from mainapp.ajax_class.utils import *
from django.core.serializers.json import DjangoJSONEncoder

from pengguna.models import Pengguna
from riwayatstudi.models import RiwayatStudi

def index(request):
    if not request.user.is_authenticated:
        print("go to login")
        return HttpResponseRedirect(reverse('mainapp:login'))
    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:dashboard'))

def my_authenticating(username, password):
    print("my_authenticating")
    user_login = None

    local_user = auth.authenticate(username=username, password=password)
    print (local_user)
    rc, message = '',''

    if local_user:
        if local_user.is_superuser:
            print ("user is ADMIN")
            user_login = local_user
            rc = "00"
            message = "this is admin"
        else:
            print ("user FOUND")
            user_login = local_user
            rc = "00"
            message = "this is user biasa"
    else:
        rc = "99"


    return user_login, rc, message

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('mainapp:index'))
    elif request.method == "POST":
        print ("POST")
        username = request.POST['username'].lower()
        password = request.POST['password']
        user, rc, message = my_authenticating(username, password)
        print ("user : ", user)
        print ("rc : ", rc)
        print ("message : ", message)

        if user is not None and rc == "00":
            print ("user is not None, go to index")
            auth_login(request, user)
            record_log(True, user.username, "login")
            return HttpResponseRedirect(reverse('mainapp:index'))
        else:
            url = 'registration/login.html'
            msg_false = 'Wrong username or password'

            context = {'msg_false': msg_false}
            return render(request, url, context)
    else:
        url = 'registration/login.html'
        return render(request, url)

@login_required()
def dashboard(request):
    html = 'mainapp/dashboard.html'

    context = {}
    context['app'] = 'mainapp'
    
    try:
        obj_pengguna = Pengguna.objects.get(user=request.user)
    except Exception as e:
        obj_pengguna = None
    
    context['pengguna'] = obj_pengguna
    profile_pengguna = Pengguna.objects.filter(user=request.user)
    context['profile'] = profile_pengguna.values()
    rwstudi = RiwayatStudi.objects.filter(fk_anggota=obj_pengguna)
    context['riwayat_studi'] = rwstudi


    keys_rwstudi = [
        'nama_instansi', 
        'nomor_induk_studi', 
        'fk_anggota',
        'negara',
        'nama_provinsi',
        'nama_kabupaten',
        'fk_jenjang_pendidikan',
    ]

    context['keys_rwstudi'] = keys_rwstudi

    keys_profile = [
        'nomor_induk_anggota',
        'nama_lengkap',
        'nama_panggilan',
        'jenis_kelamin',
        'tempat_lahir',
        'tanggal_lahir',
        'nomor_hp',
        'email',        
        'created_at',
    ]
    context['keys_profile'] = keys_profile

    print(obj_pengguna)
    print(profile_pengguna)
    print(rwstudi)

    record_log(True, request.user.username, "open " + context['app'] + " dashboard")

    return render(request, html, context)

class AjaxDatatables(View):

    def post(self, request, model):
        datas = self._process(request, model)
        return HttpResponse(json.dumps(datas, cls=DjangoJSONEncoder), content_type='application/json')

    def _process(self, request, model):
        # print ("_process: ", model)

        modelClass = get_model_class(model)

        datatables = request.POST
        params = process_params(datatables)

        draw = params['draw']
        start = params['start']
        length = params['length']
        search = params['search']
        order_col_name = params['order_col_name']

        datas = modelClass.get_all_data(request)
        records_total = datas.count()
        records_filtered = records_total

        if search:
            datas = modelClass.filter_search(datas, search)

        datas = filter_specific_column(modelClass, datas, datatables)
        datas = datas.order_by(order_col_name)

        records_total = datas.count()
        records_filtered = records_total

        object_list = process_paginator(datas, start, length)
        data = modelClass.generate_data(object_list)

        print ("data : ", data)

        return {
        	'draw': draw,
        	'recordsTotal': records_total,
        	'recordsFiltered': records_filtered,
        	'data': data,
        }