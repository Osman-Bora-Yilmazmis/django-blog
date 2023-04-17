from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import YaziGuncelleFormModel
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required #alttaki işlem için gereken kütüphaneyi import ettik

@login_required(login_url='/') #eğer kullanici giris yapmadan yazi ekleme ekranına adres üzerinden erişmek isterse onu anasayfaya yönlendirir
def yazi_guncelle(request,slug):
    
    yazi= get_object_or_404(YazilarModel, slug=slug, yazar=request.user) #giriş yapmış bir kişinin bir yazısı varsa bu slug'ta
    form = YaziGuncelleFormModel(request.POST or None, files=request.FILES or None, instance=yazi) #formumu oluştur (buradaki instance yazımızın mevcut değerlerini güncelleme ekranına getirir.)
    
    if form.is_valid():#güncelleme isteği yapıldığında girilen hatasızsa(örn: isim kısmının max karakteri 25 i gecmeyecek vs.)
        form.save()#yapılan işlemi kaydet
        return redirect('detay', slug=yazi.slug) #kullanıcıyı detay ekranına döndür
    print(slug) #kontrol amaçlı
    
    return render(request, 'pages/yazi-guncelle.html', context={
        'form': form #burada özellikleri atanmış  olan form html dosyasına gönderilir.
        
    })