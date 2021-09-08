from mainapp.utils import get_pengguna_or_none
from mainapp.models import  JenjangPendidikan

def impl_save(request, data, _POST):
    func_name = "impl_save"
    print ("#"+func_name)
    
    pengguna = get_pengguna_or_none(request)
    print(pengguna.nama_lengkap)

    data.fk_anggota = pengguna
    data.nama_instansi = _POST.get('nama_instansi')
    data.alamat_instansi = _POST.get('alamat_instansi')
    data.bidang = _POST.get('bidang')
    
    data.tahun_masuk = _POST.get('tahun_masuk')
    data.tahun_keluar = _POST.get('tahun_keluar')
    data.alasan_keluar = _POST.get('alasan_keluar')
    data.jabatan = _POST.get('jabatan')
    
    data.save()