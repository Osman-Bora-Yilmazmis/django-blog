from django import template
from blog.models import KategoriModel #sitemizde veritabanındaki kategori tiplerine erişebilmek için import edidlir

register = template.Library() #template kütüphanesi çağırılır

@register.simple_tag 
def kategori_list(): #kategori verilerine erişmemizi ve döndürmemizi sağlayan method
    kategoriler = KategoriModel.objects.all()
    return kategoriler
