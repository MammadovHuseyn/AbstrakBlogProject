from modeltranslation.translator import translator, TranslationOptions
from .models import Blog , Category 

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Blog, BlogTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title' ,)

translator.register(Category, CategoryTranslationOptions)