from django.contrib.auth.decorators import login_required
from blog.models import YorumModel
from django.shortcuts import get_object_or_404, redirect

#burada python django kütüphanesinin işlemi özetlenmiştir.
#request.user sitede işlemi yapan kullanıcıyı döndürür.

@login_required(login_url='/')
def yorum_sil(request, id): #yorumları url kısmında slug üzerinden değilde id üzerinden tuttuk ondan dolayı burada slug yerine yorumun id'sini gönderdik
    yorum = get_object_or_404(YorumModel, id=id)#id'si bizim sayfamıza yapılan yorumun  id'si olanı bulur
    if yorum.yazan ==request.user or yorum.yazi.yazar == request.user: #yorumun yazari giriş yapmış kullanıcı ise veya yazının yazarı giriş yapmış kullanıcı ise
        yorum.delete() #bu yorumu güzelce sil
        return redirect('detay', slug = yorum.yazi.slug) #daha sonra kullanıcı yazının bulundugu detay sayfasına gitsin(bunu slug= yorum.yazislug ile kontrol ettik)
    
    return redirect('anasayfa') #bu işlemlerin dışında bir işlem gerçekleşiyorsa onu direk anasayfaya yönlendir
