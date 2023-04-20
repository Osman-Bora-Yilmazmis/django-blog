from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import PasswordChangeForm #DJANGO kütüphanesinin içinde bulunan hazır password değiştirme metodu bulunur
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def sifre_degistir(request):
    if request.method == 'POST': #kullanıcı şifre değiştir butonuna tıklarsa bu koşul aktifleşir
        form = PasswordChangeForm(request.user, request.POST) #hazır bir formu kullandık
        if form.is_valid(): #gitdigi yeni sifre dogru ise
            kullanici = form.save() #yeni sifresi kaydedilir
            update_session_auth_hash(request, kullanici) #mevcut oturumu güncellenir (şifre güncellendikten sonra otomatik kullanıcıdan çıkıyordu onu önledi)
            messages.success(request, 'Şifre başarıyla güncellendi')
            return redirect('sifre-degistir') #şifre değiştirme ekranına döner
        
    else:
        form = PasswordChangeForm(request.user) #kullanıcı şifre değiştir butonuna basmazsa bu ekran gelir

    return render(request, 'pages/sifre-degistir.html', context = {
        'form': form #formu ekrana gönderir
    })