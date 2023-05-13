from django.contrib import admin
from .models import Blog , Post, Category , Comments , Contact , Settings , PostComments  , Services ,Services_category , Subscription
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class BlogAdmin(TranslationAdmin):
    list_display = ('title' , 'slug' , 'created_at' , 'updated_at', )
    list_filter = ('title' , )
admin.site.register(Blog , BlogAdmin)

class ServiceAdmin(TranslationAdmin):
    list_display = ("title", "category" )
    # list_filter = (, )
admin.site.register(Services , ServiceAdmin)

class ServiceCategoryAdmin(TranslationAdmin):
    list_display = ("title",)
admin.site.register(Services_category , ServiceCategoryAdmin)


admin.site.register(Subscription)

class CategoryAdmin(TranslationAdmin):
    list_display = ('title' , 'slug' ,)
admin.site.register(Category , CategoryAdmin)

admin.site.register(Post)
admin.site.register(PostComments)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('writer', 'comment_text')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , )

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request , obj = None):
        if request.user.username == "AdminGusi":
            return True
        else:
            return False
    
    def has_add_permission(self, request , obj = None):
        if request.user.username == "AdminGusi":
            return True
        else:
            return False
