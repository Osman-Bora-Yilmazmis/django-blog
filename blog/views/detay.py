from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel #bu import işlemini yaparak veritabanında bulunan bir veriyi alırız
from blog.forms import YorumEkleModelForm
#views ayrıca veritabanından gelen verileri ilgili html sayfaları arasında köprü görevi görür ikisinin arasındaki bağlantıyı sağlar

def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug) #ilgili veri yoksa 404 gönderir
    yorumlar = yazi.yorumlar.all() #ilgili yazinin altındaki bütün yorumları döndürür.
    
    if request.method == 'POST': #eğerki istek post isteğiyse
        yorum_ekle_form = YorumEkleModelForm(data=request.POST)
        if yorum_ekle_form.is_valid(): #geçerli bir işlem ise aşşağıdan devam et
            yorum = yorum_ekle_form.save(commit=False) # Django'da "commit", veritabanında yapılan değişiklikleri kaydetmek için kullanılan bir işlemdir. bu yüzden commiti başta false atayıp içini aşşağıdakilerle dolduruyoruz
            yorum.yazan = request.user
            yorum.yazi = yazi 
            yorum.save() #yukarıdaki veriler atandıktan veritabanına sonra kaydediyoruz
    
    yorum_ekle_form = YorumEkleModelForm()

    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar,
        'yorum_ekle_form': yorum_ekle_form

    }) #detay.html sayfamızın yolu girilir. bu metodta ilgili html sayfasına context içinde verilerimizi gönderebiliriz