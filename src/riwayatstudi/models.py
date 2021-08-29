from django.db import models
from django.contrib.auth.models import User

from mainapp.models import JenjangPendidikan
from pengguna.models import Pengguna

# Create your models here.

class RiwayatStudi(models.Model):
    
    id = models.AutoField(primary_key=True)
    fk_anggota = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    nomor_induk_studi = models.CharField(max_length=20, unique=True)
    nama_instansi = models.CharField(max_length=255)
    negara = models.CharField(max_length=255, default='INDONESIA')
    
    id_provinsi = models.CharField(max_length=10, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=100, blank=True, null=True)
    
    id_kabupaten = models.CharField(max_length=10, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=100, blank=True, null=True)

    is_indonesia = models.BooleanField(default=True)
    alamat_kampus_luar_negeri = models.TextField(blank=True, null=True)

    fk_jenjang_pendidikan = models.ForeignKey(JenjangPendidikan, verbose_name=("JenjangPendidikan"), on_delete=models.CASCADE)
    fakultas = models.CharField(max_length=255, blank=True) # untuk PT
    jurusan = models.CharField(max_length=255, blank=True) # IPA, IPS, dsb
    jalur_masuk = models.CharField(max_length=255, blank=True, null=True)
    
    tahun_masuk = models.CharField(max_length=255, blank=True, null=True)
    tahun_keluar = models.CharField(max_length=255, blank=True, null=True) 
    alasan_keluar = models.TextField(blank=True)
    is_beasiswa = models.BooleanField(null=True)
    nama_beasiswa = models.CharField(max_length=255, blank=True,null=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fk_anggota) + "-" + str(self.fk_jenjang_pendidikan)

