from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='mainapp')),    
    path('survey/', include('survey.urls', namespace='survey')),
    path('pengguna/', include('pengguna.urls', namespace='pengguna')),
    path('riwayatstudi/', include('riwayatstudi.urls', namespace='riwayatstudi')),
    path('riwayatkerja/', include('riwayatkerja.urls', namespace='riwayatkerja')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)