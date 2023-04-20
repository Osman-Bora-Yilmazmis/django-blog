from django.views.generic import DetailView #django'nun detayları görüntülememiz icin olusturdugu detay class'ı
from account.models import CustomUserModel
from django.shortcuts import get_object_or_404

class ProfilDetailView(DetailView):
    template_name = 'pages/profil.html'
    context_object_name = 'profil' #ilgili kişinin profil bilgilerine html üzerinde bu isimle erişiriz (isim,soyisim,email vs.)

    def get_object(self):
        return get_object_or_404(
            CustomUserModel, username = self.kwargs.get('username') #adres yerine (örn: http://127.0.0.1:8000/account/kullanici/root gibi gelen adresi alır eğer böyle bir kişi kayıtlı degilse 404 hatası döndür)

        )