from django.shortcuts import render, redirect 
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login, authenticate

def kayit(request):
    if request.method == 'POST':
        form = KayitFormu(request.POST) #gelen isteklerin hepsi form'a gönderilir
        if form.is_valid(): #gelen değerler on numaraysa
            form.save() #kullaniciyi kaydederiz
            username = form.cleaned_data.get('username') #girdigi username'i username'e atarız
            password = form.cleaned_data.get('password1') #girdigi sifreyi password'e atarız
            user = authenticate(username = username, password = password) #daha sonra oluşan kullanıcının passwordunu ve ismini user'da tutarız
            login(request,user) #kullanici kayit olduğu anda giriş yaptırılır ve
            return redirect('anasayfa') #anasayfa ekranına döndürülür

    else:
        form = KayitFormu()


    return render(request, 'pages/kayit.html', context = {
        'form': form
    })