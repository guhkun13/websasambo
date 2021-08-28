from django import forms

class PenggunaForm(forms.Form):
    JENIS_KELAMIN_CHOICES = (
        ('L', 'LAKI-LAKI'), 
        ('P', 'PEREMPUAN')
    )

    jenis_kelamin = forms.CharField(widget=forms.Select(choices=JENIS_KELAMIN_CHOICES),)
    nama_lengkap = forms.CharField(max_length=255)
    
    tempat_lahir = forms.CharField()
    birth_year = forms.DateField(widget=forms.SelectDateWidget())