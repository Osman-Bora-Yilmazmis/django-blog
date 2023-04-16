from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator #Sayfalama işlemi için gereken paginator kütüphanesini aktifleştirmemizi sağlar
from django.contrib.auth.decorators import login_required #login olmadan yazılarım sayfasını açmaya çalışırlarsa bu kütüphane yardımcı olucak



@login_required(login_url='/') #eğer login olmadan yazılarım sayfasını görüntülemek isterse otomatikman anasayfaya yönlendirilir
def yazilarim(request):
    

    yazilar = request.user.yazilar.order_by("-id") #siteye giren userin yazilarini azalan id ye göre sıralar (buradaki yazilar related namedir user.yazilar diyerek kullanıcının bütün yazılarına erişebilmiş olduk)
    print(yazilar) #komut satırında test etmek için yazıldı

    sayfa = request.GET.get('sayfa') #bir istek sırasında belirli bir parametrenin değerini almak için kullanılır.
    paginator = Paginator(yazilar, 1) #yazilar 2'li 2'li şekilde sıralanır 


    return render(request, 'pages/yazilarim.html', context = {
        'yazilar': paginator.get_page(sayfa),
        
    })