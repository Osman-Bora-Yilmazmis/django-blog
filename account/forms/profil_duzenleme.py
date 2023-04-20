from django.contrib.auth.forms import UserChangeForm #burada django'daki hazır profil guncelleme kutuphanesini import ediyoruz
from account.models import CustomUserModel

class ProfilDuzenlemeForm(UserChangeForm):
    password = None #şifre değiştirmeyi başka bir ekranda yaptığımızdan dolayı passwordu fieldslara dahil etmiyoruz
    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name','last_name','avatar') #buradan hangi alanları güncelleyebileceğini seçiyoruz
