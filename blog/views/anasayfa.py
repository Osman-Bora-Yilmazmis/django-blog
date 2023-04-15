from django.shortcuts import render

#sitenin anasayfasının requestleri burada bulunur ilgili sayfayanın başlığına giren kişiyi render metodundaki html adresine yönlendirir.
def anasayfa(request):
    context = {
        'isim' : 'OSMAN BORA YILMAZMIŞ'
    }
    return render(request, 'pages/anasayfa.html', context = context)
