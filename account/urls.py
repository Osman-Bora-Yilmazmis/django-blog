from django.urls import path
from account.views import cikis, sifre_degistir, profil_guncelle, kayit, ProfilDetailView
from django.contrib.auth import views as auth_views #django'nun icinde hazır olarak bulunan viewların hepsini sectik. bizim burada kullanacagımız ise login view 
#auth_views class based view olarak tasarlanmıstır.

urlpatterns = [
    path('cikis',cikis, name='cikis'), #sidebar'da tanımladık (cikis url sine gidip buraya yönlendirildi buraya yönlendirilen request daha sonra cikis.py ye gidip onu çalıştırdı.)
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit', kayit, name='kayit'),
    path('kullanici/<str:username>',ProfilDetailView.as_view(),name='profil'),
    #altta yaptığımız işlemde giriş yapma view'i oluşturmadan django'nun hazır olarak sundugu giris viewini kullandık
    path('giris',auth_views.LoginView.as_view( #Login formunu görüntüler/ class based viewleri kodumuzda .as_view() diyerek kullanıyoruz. 
        template_name = 'pages/giris.html' #LoginView'de bulunan hazır giriş ekranını giris.html dosyamıza yönlendiriyoruz
    ), name='giris')

]   