from django.db import models
from django.contrib.auth.models import User

from mainapp.models import JenjangPendidikan

# Create your models here.
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
    fk_ijazah_tertinggi = models.ForeignKey(JenjangPendidikan, verbose_name='Ijazah Tertinggi', on_delete=models.CASCADE, null=True, blank=True, default=None)

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
