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

class JenjangPendidikan(models.Model):
    PMA = 'PENDIDIKAN MENENGAH ATAS'
    PT = 'PERGURUAN TINGGI'

    JENIS_JENJANG_CHOICES = (
        ('PT', PT), 
        ('PMA', PMA)
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


# PENGGUNA

class Pengguna(models.Model):
    JENIS_KELAMIN_CHOICES = (('L', 'LAKI-LAKI'), ('P', 'PEREMPUAN'))
    AGAMA_CHOICES = (
        ('ISLAM', 'ISLAM'), 
        ('KRISTEN', 'KRISTEN'),
        ('KATOLIK', 'KATOLIK'),
        ('HINDU', 'HINDU'),
        ('BUDDHA', 'BUDDHA'),
        ('KONGHUCU', 'KONGHUCU')
    )

    id = models.AutoField(primary_key=True)
    nomor_induk_anggota = models.CharField(max_length=20, unique=True)
    nama_lengkap = models.CharField(max_length=255)
    nama_panggilan = models.CharField(max_length=255, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=25, choices = JENIS_KELAMIN_CHOICES, default='')
    agama =  models.CharField(max_length=100, choices = AGAMA_CHOICES, default='', null=True, blank=True)
    tempat_lahir = models.CharField(max_length=255, blank=True, null=True)
    tanggal_lahir = models.DateField()
    fk_ijazah_tertinggi = models.ForeignKey('JenjangPendidikan', verbose_name='Ijazah Tertinggi', on_delete=models.CASCADE, null=True, blank=True, default=None)

    nomor_hp = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField( max_length=254, unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)  # OneToOneField means, FK is unique
     
    desc = models.TextField(blank=True)
    is_delete = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_lengkap + "-" + self.email


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

    fk_jenjang_pendidikan = models.ForeignKey("JenjangPendidikan", verbose_name=("JenjangPendidikan"), on_delete=models.CASCADE)
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

