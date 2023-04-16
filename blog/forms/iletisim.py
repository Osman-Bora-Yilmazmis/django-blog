from django import forms #bu class sayesinde kullanıcıların bilgi gönderebilecği form elemanları oluşturabiliyoruz  
#bu class sayesinde formlar bize otomatik olarak html çıktısı üretecek
#bu html çıktısı üzerinde çeşitli validasyonlar uygulanacak
#django kullanıcının girdiği formdaki fieldları otomatik algılayıp bu form üzerinde validasyonlar gerçekleştiricek
from blog.models import IletisimModel #kodu kısaltır isimizi kolaylastırır assagıda kullandık

#kullanıcının karşısına çıkacak form fieldları burada bulunur
class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ['isim_soyisim','email','mesaj']
