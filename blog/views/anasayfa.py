from django.shortcuts import render # render kısmı gelen http adresini almamızı sağlayan fonksiyonu içerir
from blog.models import YazilarModel
from django.core.paginator import Paginator #Sayfalama işlemi için gereken paginator kütüphanesini aktifleştirmemizi sağlar
from django.db.models import Q #import ettiğim Q değişkeni 'or' anlamı taşıamktadır.

#WIEWS KISMI HAKKINDA BİLGİ:
#burasi kullanıcının adres sahasına girdiği site adresini kontrol etmek amaçlı kullanılır
#kullaniciyi sayfaya yönlendirmeden önce sayfanın özelliklerini belirlememize olanak sağlar
# özetle views dosyası içinde biz ekranda çıkacak sayfanın özelliklerini kısıtlamalarını adreslerini kontrol ediyoruz.


#sitenin anasayfasının requestleri burada bulunur ilgili sayfayanın başlığına giren kişiyi render metodundaki html adresine yönlendirir.
def anasayfa(request):
    sorgu = request.GET.get('sorgu') #buradaki get kullanıcının adres yerine yazdığı kelimedir
    print(sorgu) #gelen sorgunun kontrolü (örnek: http://127.0.0.1:8000/?sorgu=html buradaki 'sorgu=' den sonra gelen html yazisini tutar)
    
    yazilar = YazilarModel.objects.order_by('-id') #yazi objelerini id si azalan şekilde sıralar
    
    if sorgu:
        yazilar = yazilar.filter(#adres alanındaki sorguya göre filtre işlemi gerçekleştirilir.
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        ).distinct() #eğer aynı veri sorgu esnasında birden fazla gelirse birini döndürür
    
    
    sayfa = request.GET.get('sayfa') #bir istek sırasında belirli bir parametrenin değerini almak için kullanılır.
    paginator = Paginator(yazilar, 2) #yazilar 2'li 2'li şekilde sıralanır 


    return render(request, 'pages/anasayfa.html', context = {
        'yazilar': paginator.get_page(sayfa)
    })
