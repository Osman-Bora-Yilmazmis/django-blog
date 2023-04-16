from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm()

    if request.method == 'POST': #HTML sayfasında kullanıcının iletisim bilgilerini girdigi alanın metoduna eriştik 
        form = IletisimForm(request.POST) #kullanıcının siteye girdiği form bilgilerini form objesine atadık
        if form.is_valid(): #girilen veriler geçerliyse aşağıda verilir tek tek alınır kaydedilir ve admine gönderilir
            form.save()#forms dosyasındaki iletisim.py de import ettigimiz models formu otomatik IletisimModel'den database kaydı oluşturuyor 
            return redirect('anasayfa') #işlem bitince anasayfaya dönülür
              
    context = {
        'form': form
    }
    return render(request, 'pages/iletisim.html', context= context) #baştaki html dosyası sayfanın template'ini belirliyor yanındaki context ise kullanılacak attributeleri veya tabloları html'e gönderiyor sayfadan işlem yapabiliyoruz gelen verilerle