from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


#MASTER DATA
class Log(models.Model):
    id = models.AutoField(primary_key=True)    
    user = models.CharField(max_length=100, blank=True, null=True)    
    info = models.TextField(blank=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id




## MASTER DATA MODUL KUISIONER ##
class TipeJawabanDanPertanyaan(models.Model):
    id = models.AutoField(primary_key=True)    
    kode = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=50, unique=True)
    
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama + "-" + self.desc

class ModulInduk(models.Model):
    id = models.AutoField(primary_key=True)
    kode_modul = models.CharField(max_length=50)
    judul_modul = models.CharField(max_length=255)
    
    desc = models.TextField(blank=True) 
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kode_modul + "-" +self.judul_modul

class ModulOpsiJawaban(models.Model):
    id = models.AutoField(primary_key=True)
    fk_modul_induk = models.ForeignKey(ModulInduk, on_delete=models.CASCADE)
    kode_modul = models.CharField(max_length=50)
    kode_kunci = models.CharField(max_length=50)
    teks_jawaban = models.TextField(blank=True)
    fk_tipe_jawaban = models.ForeignKey(TipeJawabanDanPertanyaan, on_delete=models.CASCADE)
    urutan = models.IntegerField(blank=True, null=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kode_modul + "-" +self.kode_kunci + "-" +self.teks_jawaban + "-" +str(self.fk_tipe_jawaban )


class ModulPertanyaan(models.Model):
    id = models.AutoField(primary_key=True)
    fk_modul_induk = models.ForeignKey(ModulInduk, on_delete=models.CASCADE)
    kode_pertanyaan = models.CharField(max_length=50, unique=True)
    teks_pertanyaan = models.TextField(blank=True)
    fk_tipe_pertanyaan = models.ForeignKey(TipeJawabanDanPertanyaan, on_delete=models.CASCADE)
    urutan = models.IntegerField(blank=True, null=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kode_pertanyaan + "-" + self.teks_pertanyaan + "-" + str(self.fk_tipe_pertanyaan)


class JenjangPendidikan(models.Model):
    PMA = 'PENDIDIKAN MENENGAH ATAS'
    PT = 'PERGURUAN TINGGI'

    JENIS_JENJANG_CHOICES = (
        ('PMA', PMA),
        ('PT', PT)
    )

    id = models.AutoField(primary_key=True)
    kode = models.CharField(max_length=100, unique=True)
    nama = models.CharField(max_length=255)
    jenis = models.CharField(max_length=200, choices = JENIS_JENJANG_CHOICES, default='')
    urutan = models.IntegerField(blank=True, null=True)
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kode + "-" +self.nama + "-" +self.desc
    
    # Pendidikan Menengah Atas:
    # SMA, MA, 

    # Perguruan Tinggi :
    # D1 - S3
    