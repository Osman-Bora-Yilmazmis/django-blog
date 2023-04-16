from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim

#Burası

urlpatterns = [
    path('', anasayfa, name= 'anasayfa'),#name etiketine yazdığımız isimle html kodlarımızda bu isme erişebiliriz
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>',kategori, name='kategori'),#kategori yazısının yanına /asdad gibi rastgele değer girilirse bile anasayfaya yönlendirir. yani kategori isminde bir link tanımlandı
    path('yazilarim', yazilarim, name='yazilarim')
]
