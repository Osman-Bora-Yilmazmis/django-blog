from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator #Sayfalama işlemi için gereken paginator kütüphanesini aktifleştirmemizi sağlar


#sitenin anasayfasının requestleri burada bulunur ilgili sayfayanın başlığına giren kişiyi render metodundaki html adresine yönlendirir.
def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug) #eğer adrsin yanına girilen kategori sistemde bulunmuyors 404 hatası döndürür bulunuyorsa ilgili sayfa açılır
    
    yazilar = kategori.yazi.order_by("-id") #aratılan kategorideki yazıları, (veri tabanında varsa eğer) verileri döndürür.
    print(yazilar) #komut satırında test etmek için yazıldı

    sayfa = request.GET.get('sayfa') #bir istek sırasında belirli bir parametrenin değerini almak için kullanılır.
    paginator = Paginator(yazilar, 2) #yazilar 2'li 2'li şekilde sıralanır 


    return render(request, 'pages/kategori.html', context = {
        'yazilar': paginator.get_page(sayfa),
        'kategori_isim': kategori.isim
    })
