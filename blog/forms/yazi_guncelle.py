from django import forms
from blog.models import YazilarModel

class YaziGuncelleFormModel(forms.ModelForm):
    class Meta:
        model= YazilarModel
        exclude = ('yazar','slug')#exclude karşısına yazılan sahalar dışında bütün sahaları alır.