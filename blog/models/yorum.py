from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel

class YorumModel(models.Model):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete = models.CASCADE, related_name='yorum') #yorum yazan kişiyi user a bağladık yazan kişi db den silinirse yorum silinecek ayrıca yazan kişinin yorumlarına erişebilmek için related_name = 'yorum' yaptık. 
    yazi = models.ForeignKey(YazilarModel, on_delete = models.CASCADE, related_name = 'yorumlar')
    yorum = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add = True)
    guncellenme_tarihi = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
    def __str__(self):
        return self.yazan.username