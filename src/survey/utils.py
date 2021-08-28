import json

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from mainapp.models import *

import datetime


def get_obj_provinsi(id):
	try:
		res = DaftarProvinsi.objects.get(pk=id)
	except Exception as e:
		res = None
	
	return res

def get_obj_kabupaten(id):
	try:
		res = DaftarKabupaten.objects.get(pk=id)
	except Exception as e:
		res = None

	return res

def get_obj_jenjang_pendidikan(id):
	try:
		res = JenjangPendidikan.objects.get(pk=id)
	except Exception as e:
		res = None

	return res

	
