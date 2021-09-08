from django.db import models
from pengguna.models import Pengguna

# Create your models here.
class RiwayatKerja(models.Model):
    
    id = models.AutoField(primary_key=True)
    fk_anggota = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    nama_instansi = models.CharField(max_length=255)
    alamat_instansi = models.TextField(blank=True, null=True)
    bidang = models.CharField(max_length=255, blank=True, null=True) # untuk PT
    
    tahun_masuk = models.CharField(max_length=255, blank=True, null=True)
    tahun_keluar = models.CharField(max_length=255, blank=True, null=True) 
    alasan_keluar = models.TextField(blank=True)
    jabatan = models.CharField(max_length=255, blank=True, null=True) 
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fk_anggota) + "-" + str(self.nama_instansi)

