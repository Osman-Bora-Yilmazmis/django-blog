from django.urls import path, include
from blog.views import IletisimFormView, anasayfa, KategoriListView, yazilarim, DetayView, YaziEkleCreateView, YaziGuncelleUpdateView, YazıSilDeleteView, yorum_sil
from django.views.generic import TemplateView, RedirectView #RedirectView kullanciyi ilgili adrese yönlendiri.
#Burası sayfa adreslerinin oluşturulduğu bölümdür 
#ilgili sayfa ismini views içinde bulunan (örn: anasayfa.py dosyasıyla) eşleştiririz ve bu eşleştirme sonucunda
# anasayfa.py dosyasına html kodlarımız içinde erişip gelen verileri kullanabiliriz 


#ayrıca gidilecek sayfanın http formatını oluştururuz
#(örn: http://127.0.0.1:8000/kategori/python-dersleri şeklinde o sayfaya giderim eğer böyle bir ders varsa)
#(örn: http://127.0.0.1:8000/anasayfa)

urlpatterns = [
    path('', anasayfa, name= 'anasayfa'),#name etiketine yazdığımız isimle html kodlarımızda bu isme erişebiliriz
    path('iletisim', IletisimFormView.as_view(), name='iletisim'),
    path('kategori/<slug:kategoriSlug>',KategoriListView.as_view(), name='kategori'),#kategori yazısının yanına /asdad gibi rastgele değer girilirse bile anasayfaya yönlendirir. yani kategori isminde bir link tanımlandı
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>',DetayView.as_view(), name='detay'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>',YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', YazıSilDeleteView.as_view(), name='yazi-sil'),
    path('yorum-sil/<int:id>',yorum_sil, name='yorum-sil'),
    path('hakkimda', TemplateView.as_view( #kullanici hakkimda sayfasına geldiginde hakkimda.html otomatik olarak render edilecek. as_view dedigimizde view dosyası oluşturmadan url ve html  arasında sayfa bağlantısı oluşturulur
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),
    path('yonlendir', RedirectView.as_view( #kullanıcı adres kısmına /yonlendir eklerse google sayfasına yonlendirecek
        url = 'https://www.google.com'
    ), name='yonlendir'),
    path('email-gonderildi', TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ), name='email-gonderildi'),

]
