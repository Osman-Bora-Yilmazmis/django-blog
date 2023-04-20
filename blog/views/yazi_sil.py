from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView #django'nun içerisinde bulunan baseclass'tır yazi silme işleminde onay ekranı karsimiza cıkarmamızda bize yardımcı olur
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class YazıSilDeleteView(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi-sil-onay.html'#silme işlemi yapıldıgında karsımıza cıkacak uyarı  mesajı'nın html adresini tutar
    success_url = reverse_lazy('yazilarim') #islem bittikten sonra bu sayfaya döndürür

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'], yazar = self.request.user) #silmek istedigimiz yazıyı tutar. (parantez icinde ilgili  yazının slug'ını ve silen kişinin kullanıcı olup olmadıgını kontrol ettik)
        return yazi


#aşşağıdaki'de kullanılabilir
"""
@login_required(login_url='/')
def yazi_sil(request, slug):
    get_object_or_404(YazilarModel, slug=slug, yazar = request.user).delete()
    return redirect('yazilarim')
"""