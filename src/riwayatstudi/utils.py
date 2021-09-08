from mainapp.utils import get_pengguna_or_none
from mainapp.models import  JenjangPendidikan

def impl_save(request, data, _POST):
    func_name = "impl_save"
    print ("#"+func_name)
    # create new
    pengguna = get_pengguna_or_none(request)
    print(pengguna.nama_lengkap)

    data.fk_anggota = pengguna
    data.nomor_induk_studi = _POST.get('nomor_induk_studi')
    data.nama_instansi = _POST.get('nama_instansi')
    negara = _POST.get('negara', 'INDONESIA')
    data.negara = negara
    
    is_indo = False
    if negara == 'INDONESIA':
        is_indo = True

    data.is_indonesia = is_indo
    alamat_kampus_luar_negeri = ''
         
    if not is_indo:
        data.id_provinsi = ''
        data.nama_provinsi = ''
        data.id_kabupaten = ''
        data.nama_kabupaten = ''
        alamat_kampus_luar_negeri = _POST.get('alamat_kampus_luar_negeri')

    else:
        tempprov = _POST.get('provinsi').split('|')
        print("tempprov = ", tempprov)
        data.id_provinsi = tempprov[0]
        data.nama_provinsi = tempprov[1]

        tempkab = _POST.get('kabupaten').split('|')
        print("tempkab = ", tempkab)
        data.id_kabupaten = tempkab[0]
        data.nama_kabupaten = tempkab[1]                

    data.alamat_kampus_luar_negeri = alamat_kampus_luar_negeri
    
    temp_jenjang_pendidikan = _POST.get('jenjang_pendidikan')
    temp_jenjang_pendidikan = temp_jenjang_pendidikan.split('|')
    id_jenjang_pendidikan = temp_jenjang_pendidikan[0]
    nama_jenjang_pendidikan = temp_jenjang_pendidikan[1]

    jenjang_pendidikan = JenjangPendidikan.objects.get(pk=id_jenjang_pendidikan)
    data.fk_jenjang_pendidikan = jenjang_pendidikan

    fakultas = _POST.get('fakultas')
    if jenjang_pendidikan.jenis == 'PMA':
        fakultas = ''
        
    data.fakultas = fakultas
    data.jurusan = _POST.get('jurusan')
    data.jalur_masuk = _POST.get('jalur_masuk')
    data.tahun_masuk = _POST.get('tahun_masuk')
    data.tahun_keluar = _POST.get('tahun_keluar')
    data.alasan_keluar = _POST.get('alasan_keluar')
    
    is_beasiswa = _POST.get('is_beasiswa')
    nama_beasiswa = _POST.get('nama_beasiswa')
    data.is_beasiswa = is_beasiswa
    if is_beasiswa:
        data.nama_beasiswa = nama_beasiswa
    data.save()