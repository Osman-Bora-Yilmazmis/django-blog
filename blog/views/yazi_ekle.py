from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required #alttaki işlem için gereken kütüphaneyi import ettik
from django.views.generic import CreateView #django'nun içerisinde bulunan hazır base class
from blog.models import YazilarModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #kullanicinin giriş yapmadan yazi eklemesini engelleyen kütüphane

class YaziEkleCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('giris') #kullanici giris yapmadan yazi eklemeye kalkarsa giris ekranına döndürülür
    template_name = 'pages/yazi-ekle.html'  #yazi ekleme formunun html adresini belirler
    model = YazilarModel #hangi model üzerinde kayıt gerçekleştireceğimizi yazıyoruz
    fields = ('baslik','icerik','resim','kategoriler') #gelen modelden, yazıyı oluştururken hangi basliklari dolduracagımız seciyoruz

    def get_success_url(self): #ilgili yazı oluşturulduktan sonra oluşan yazının detay ekranını getirir.
        return reverse('detay',kwargs={
            'slug': self.object.slug})

    def form_valid(self, form): #form validse bu işlemleri gerçekleştir
        yazi = form.save(commit = False)
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m()
        return super().form_valid(form) #yukarıda yapılan değişiklikleri super() ile form_valid'in içine veriyoruz



"""
@login_required(login_url='/') #eğer kullanici giris yapmadan yazi ekleme ekranına adres üzerinden erişmek isterse onu anasayfaya yönlendirir
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit = False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug=yazi.slug)
    
    
    return render(request, 'pages/yazi-ekle.html', context={
        'form': form #yazi-ekle.html sayfasına form key'ini gönderip html dosyaı içinde bu keyi kullanabiliriz
    })
"""