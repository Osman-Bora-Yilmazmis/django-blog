from django.db import models

class DateAbstractModel(models.Model): #BU CLASS ta yorum.py ve yazi.py de tekrarlı kullanılan attributeleri soyut bir sınıf üzerinde tanımladık ikiside bu soyut sınıf uzerinden attributelerine erisiyor
    olusturulma_tarihi = models.DateTimeField(auto_now_add = True)
    duzenlenme_tarihi = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True