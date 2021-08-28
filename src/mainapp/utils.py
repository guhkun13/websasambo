import json

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import *

import datetime


def get_data_dashboard():
	data_admin = {}

	#ProdiBaru
	prodi_barus = ProdiBaru.objects.all()
	count_prodi_barus = prodi_barus.count()
	if count_prodi_barus > 0:
		last_prodi_baru = prodi_barus.order_by('-created_at')[0].created_at.date()
	else:
		last_prodi_baru = '-'

	#BianglalaNew
	bianglala_news = BianglalaNew.objects.all()
	count_bianglala_news = bianglala_news.count()
	if count_bianglala_news > 0:
		last_bianglala_new = bianglala_news.order_by('-created_at')[0].created_at.date()
	else:
		last_bianglala_new = '-'

	#AIPT
	aipts = AIPT.objects.all()
	count_aipts = aipts.count()
	if count_aipts > 0:
		last_aipt = aipts.order_by('-created_at')[0].created_at.date()
	else:
		last_last_aipt = '-'

	#Logs
	logs = Log.objects.all().order_by('-created_at')
	count_logs = logs.count()
	if count_logs > 0:
		ten_last_logs = logs.order_by('-created_at')[:10]
	else:
		ten_last_logs = None

	result = {
		'count_prodi_barus' : count_prodi_barus,
		'count_bianglala_news' : count_bianglala_news,
		'count_aipts' : count_aipts,
		'count_logs' : count_logs,
		'ten_last_log' : ten_last_logs
	}

	return result

def record_log(state, user, desc):
	status = "Sukses"
	if not state:
		status = "Gagal"

	desc = status + '; ' + desc

	log = Log()
	log.user = user
	log.desc = desc
	log.save()


def get_all_object_properties(object):
	fields = object._meta.get_fields()
	desc = {}
	for field in fields:
	    f_name = field.name
	    f_val = getattr(object, field.name)
	    desc[f_name] = str(f_val)

	return desc

def get_current_status(obj):
	status = obj.status_verifikasi

	if status == 'verified':
		color = "green"
	elif status == 'reject':
		color = "red"
	else:
		color = "blue"

	result = {}
	result['color'] = color

	return result

def get_object_model_name(obj):
	return obj._meta.object_name


def get_pengguna_or_none(request):
	try:
		result = Pengguna.objects.get(user=request.user)
	except Exception as e:
		result = None

	return result

def get_last_log_verifikasi(object):
	try:
		result = LogVerifikasi.objects.filter(id_model=object.id).last()
	except Exception as e:
		result = None

	return result

def change_status_to_open(obj):

	try:
		obj.status_verifikasi = 'open'
		obj.save()
	except Exception as e:
	    raise e

def update_status_verifikasi_data(request, obj):
	try:
		status_verifikasi = request.POST.getlist('status_verifikasi')[0]
		obj.status_verifikasi = status_verifikasi
		obj.save()
	except Exception as e:
		raise e

def save_log_verifikasi(request, obj):
	catatan = request.POST.get('catatan')
	status_verifikasi = request.POST.getlist('status_verifikasi')[0]
	model_name = get_object_model_name(obj)

	try:
	    log_verifikasi = LogVerifikasi()
	    log_verifikasi.user = request.user.username
	    log_verifikasi.id_model = str(obj.id)
	    log_verifikasi.model_name = model_name
	    log_verifikasi.status_verifikasi = status_verifikasi
	    log_verifikasi.catatan = catatan
	    log_verifikasi.save()

	except Exception as e:
	    raise e

def split_rentang_tanggal(rentang_tanggal):
    rentang = rentang_tanggal.split('-')
    tanggal_awal = rentang[0].replace(' ','')
    tanggal_akhir = rentang[1].replace(' ','')

    return tanggal_awal, tanggal_akhir

# Date
def date_now():
    return datetime.datetime.now().date()

def convert_string_to_datetime(string, format):
    result = datetime.datetime.strptime(string, format)
    return result

def convert_datetime_to_string(datetime_object, format):
    result = datetime_object.strftime(format)
    return result

def set_datetime_to_last_time(dt):
    result = dt.replace(hour=23, minute=59)
    return result
