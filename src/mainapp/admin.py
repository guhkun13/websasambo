from django.contrib import admin

# Register your models here.
from .models import *

# Master Data
admin.site.register(Log)

# Master Data Kuisioner
admin.site.register(TipeJawabanDanPertanyaan)
admin.site.register(ModulInduk)
admin.site.register(ModulOpsiJawaban)
admin.site.register(ModulPertanyaan)
admin.site.register(JenjangPendidikan)

