from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

@admin.register(CustomUserModel) #admin.site.register(CustomUserModel,CustomAdmin) olarakta kullanabilirsin aynı özelliğe sahip
class CustomAdmin(UserAdmin):
    list_display = ('username','email')
    fieldsets = UserAdmin.fieldsets + ( #UserAdmin deki fieldsets leri inherit ettik üzerine ekstra avatar değiştirme alanı ekledik
        ('Avatar Değiştirme Alanı ',{ #bunu yapmamızın nedeni avatar attribute ünün default olarak gelmemesi 
            'fields': ['avatar']
        }),
    )


