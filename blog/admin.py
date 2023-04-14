from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

# Register your models here.

admin.site.register(KategoriModel)#Kategoriler kısmı

class YazilarAdmin(admin.ModelAdmin): #admin panelinde yazılar kısmını customize etmemizi sağlar
    search_fields = ('baslik', 'icerik')
    list_display= (
        'baslik', 'oluşturulma_tarihi', 'duzenleme_tarihi'
    )

admin.site.register(YazilarModel,YazilarAdmin)#Yazılar kısmı