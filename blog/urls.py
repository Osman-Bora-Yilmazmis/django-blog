from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil

#Burası sayfa adreslerinin oluşturulduğu bölümdür 
#ilgili sayfa ismini views içinde bulunan (örn: anasayfa.py dosyasıyla) eşleştiririz ve bu eşleştirme sonucunda
# anasayfa.py dosyasına html kodlarımız içinde erişip gelen verileri kullanabiliriz 


#ayrıca gidilecek sayfanın http formatını oluştururuz
#(örn: http://127.0.0.1:8000/kategori/python-dersleri şeklinde o sayfaya giderim eğer böyle bir ders varsa)
#(örn: http://127.0.0.1:8000/anasayfa)

urlpatterns = [
    path('', anasayfa, name= 'anasayfa'),#name etiketine yazdığımız isimle html kodlarımızda bu isme erişebiliriz
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>',kategori, name='kategori'),#kategori yazısının yanına /asdad gibi rastgele değer girilirse bile anasayfaya yönlendirir. yani kategori isminde bir link tanımlandı
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>',detay, name='detay'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>',yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>',yazi_sil, name='yazi-sil'),
]
