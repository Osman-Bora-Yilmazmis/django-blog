from django.contrib.auth.forms import UserCreationForm #django kütüphanesinde hazır olarak bulunan bir kayıt formunu import ettik
from account.models import CustomUserModel

class KayitFormu(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ( #giriş yaparken hangi sahaları doldurabileceğini sectik
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )