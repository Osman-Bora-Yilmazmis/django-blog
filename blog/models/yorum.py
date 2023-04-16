from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel
from blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete = models.CASCADE, related_name='yorum') #yorum yazan kişiyi user a bağladık yazan kişi db den silinirse yorum silinecek ayrıca yazan kişinin yorumlarına erişebilmek için related_name = 'yorum' yaptık. 
    yazi = models.ForeignKey(YazilarModel, on_delete = models.CASCADE, related_name = 'yorumlar')
    yorum = models.TextField() 
   

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
    def __str__(self):
        return self.yazan.username