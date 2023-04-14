from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel #kategoriler attribute ü için
from django.contrib.auth.models import User #yazar attribute ü için
from ckeditor.fields import RichTextField 

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    oluşturulma_tarihi = models.DateTimeField(auto_now_add=True) #Kayıt oluşturulduğu anda oluşturulan tarih oto kaydedilir
    duzenleme_tarihi = models.DateTimeField(auto_now=True) #Kayıt düzenlendiğinde oto olarak düzenlenme tarihi alanı değişir
    slug = AutoSlugField(populate_from = 'baslik', unique=True) #www.oguzhancelikarslan.com/yazilar/pguzhan-celikarslan-kimdir? diye baslik olusturmamızı sağlar
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') #Bir yazının birden fazla kategoriye atanmasını sağlar
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazilar')#on_delete-> yazar silinirse bütün yazilarini siler

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'
    
    def __str__(self):
        return self.baslik