from django.contrib import admin
from django.urls import path, include
from blog.views import iletisim
from django.conf.urls.static import static #otomatik olarak medya dosyalarının yayınlanmasını sağlayan fonksiyon
from django.conf import settings #Lazysettings yöntemiyle settingsteki media root ve media url'i dahil etmiş olduk 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')) #eğer baştaki yorum satırına hiçbir şey tanımlanmazsa o sayfayı anasayfa yapar
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #userlar avatarlarını güncelleyebilir
