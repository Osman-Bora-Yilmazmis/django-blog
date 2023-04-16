from django.shortcuts import render

def iletisim(request):
    context = {
        'key': 'baslik icerik naber'
    }
    return render(request, 'pages/iletisim.html', context= context) #baştaki html dosyası sayfanın template'ini belirliyor yanındaki context ise kullanılacak attributeleri veya tabloları html'e gönderiyor sayfadan işlem yapabiliyoruz gelen verilerle