from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm #account'un içinde bulunan profil duzenleme formunu import ettik

@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':

        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance = request.user) #instance = request.user dedğimiz kısımda kişinin mevcut bilgileri textbox'ların içine yazılır.
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil Guncellendi')
    else:
        form = ProfilDuzenlemeForm(instance = request.user)
    return render(request, 'pages/profil-guncelle.html', context = {
        'form':form
    })