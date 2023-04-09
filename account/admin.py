from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Change Avatar', {
            "fields": (
                    ['avatar']               
                
            ),
        }),
    )
    
    
