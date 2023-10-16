from django.contrib import admin
from .models import Article, Images, Category

# registering all tables
admin.site.register(Article)
admin.site.register(Images)
admin.site.register(Category)
