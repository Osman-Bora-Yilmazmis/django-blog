from django.shortcuts import render, get_object_or_404 , redirect
from blog.models import YazilarModel #bu import işlemini yaparak veritabanında bulunan bir veriyi alırız
from blog.forms import YorumEkleModelForm
from django.views import View #bu kütüphane sayesınde get ve post islemlerini methodun içine aktararak daha anlaşılır bir kod sayfası oluşturduk.
from django.contrib import messages #yorum eklendikten sonra gelen bildirim mesajı

class DetayView(View): #View'ı çağırıyoruz view'ın içindeki get'i ve post'u kullanıyoruz
    http_method_names = ['get','post']
    yorum_ekleme_formu = YorumEkleModelForm

    def get(self, request, slug): #ekranda yorumların gözükmesine olanak sağlar
        yazi = get_object_or_404(YazilarModel, slug=slug) #ilgili veri yoksa 404 gönderir
        yorumlar = yazi.yorumlar.all() #ilgili yazinin altındaki bütün yorumları döndürür.
        return render(request, 'pages/detay.html', context={
            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorum_ekle_form': self.yorum_ekleme_formu,

        })#detay.html sayfamızın yolu girilir. bu metodta ilgili html sayfasına context içinde verilerimizi gönderebiliriz
    
    def post(self,request,slug): #kullanicinin yorum girmesine olanak sağlar
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekle_form = self.yorum_ekleme_formu(data = request.POST)
        if yorum_ekle_form.is_valid(): #geçerli bir işlem ise aşşağıdan devam et
            yorum = yorum_ekle_form.save(commit=False) # Django'da "commit", veritabanında yapılan değişiklikleri kaydetmek için kullanılan bir işlemdir. bu yüzden commiti başta false atayıp içini aşşağıdakilerle dolduruyoruz
            yorum.yazan = request.user
            yorum.yazi = yazi 
            yorum.save() #yukarıdaki veriler atandıktan veritabanına sonra kaydediyoruz
            messages.success(request, 'Yorum başarılı bir şekilde eklendi.')
        return redirect('detay', slug=slug)

#views ayrıca veritabanından gelen verileri ilgili html sayfaları arasında köprü görevi görür ikisinin arasındaki bağlantıyı sağlar

