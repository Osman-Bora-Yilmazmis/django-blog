from django.contrib.auth import logout #çıkış yapmamızı sağlayan metodu içerir aşağıda onu kullandık
from django.shortcuts import redirect

def cikis(request):  
    logout(request) #url' den gelen istek kullanıcıya çıkış yaptırdı
    return redirect('anasayfa')# ve anasayfaya döndürdü