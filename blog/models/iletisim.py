from django.db import models

class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add = True)
    


    class Meta:
        db_table = 'iletisim'
        verbose_name = 'iletisim'
        verbose_name_plural = 'iletisim'
    
    def __str__(self):
        return self.email