from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel #bu import işlemini yaparak veritabanında bulunan bir veriyi alırız

#views ayrıca veritabanından gelen verileri ilgili html sayfaları arasında köprü görevi görür ikisinin arasındaki bağlantıyı sağlar

def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug) #ilgili veri yoksa 404 gönderir
    yorumlar = yazi.yorumlar.all() #ilgili yazinin altındaki bütün yorumları döndürür.
    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar

    }) #detay.html sayfamızın yolu girilir. bu metodta ilgili html sayfasına context içinde verilerimizi gönderebiliriz