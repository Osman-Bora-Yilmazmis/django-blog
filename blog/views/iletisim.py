from django.shortcuts import render

def iletisim(request):
    return render(request, 'pages/iletisim.html', context= {}) #baştaki html dosyası sayfanın template'ini belirliyor yanındaki context ise kullanılacak attributeleri veya tabloları html'e gönderiyor sayfadan işlem yapabiliyoruz gelen verilerle