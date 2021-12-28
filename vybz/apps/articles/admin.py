from django.contrib import admin
from django.db.models import fields
from . import models

# Register your models here.


# @admin.register(models.Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'added_on')
#     search_fields = ["name"]
#     ordering = ["name"]

admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.Tag)