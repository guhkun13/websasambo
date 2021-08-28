from django.db import models
from django.contrib.auth.models import User

from mainapp.models import JenjangPendidikan
from pengguna.models import Pengguna

# Create your models here.

class RiwayatStudi(models.Model):
    
    id = models.AutoField(primary_key=True)
    fk_anggota = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    nama_instansi = models.CharField(max_length=255)
    nomor_induk_studi = models.CharField(max_length=20, unique=True)
    negara = models.CharField(max_length=255, default='INDONESIA')
    provinsi = models.CharField(max_length=255, blank=True, null=True)
    kabupaten = models.CharField(max_length=255, blank=True, null=True)

    is_indonesia = models.BooleanField(default=True)
    alamat_kampus_luar_negeri = models.CharField(max_length=255, blank=True, null=True)

    fk_jenjang_pendidikan = models.ForeignKey(JenjangPendidikan, verbose_name=("JenjangPendidikan"), on_delete=models.CASCADE)
    fakultas = models.CharField(max_length=255, blank=True) # untuk PT
    jurusan = models.CharField(max_length=255, blank=True) # IPA, IPS, dsb
    jalur_masuk = models.CharField(max_length=255, blank=True, null=True)
    tahun_masuk = models.DateField()
    tahun_keluar = models.DateField(null=True, blank=True)
    alasan_keluar = models.TextField(blank=True)
    is_beasiswa = models.BooleanField(null=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fk_anggota) + "-" + str(self.fk_jenjang_pendidikan)

