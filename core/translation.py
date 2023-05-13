from modeltranslation.translator import translator, TranslationOptions
from .models import Blog , Category , Services, Services_category

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Blog, BlogTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title' ,)

translator.register(Category, CategoryTranslationOptions)

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Services, ServiceTranslationOptions)

class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title' ,)

translator.register(Services_category, ServiceCategoryTranslationOptions)