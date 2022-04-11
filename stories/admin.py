from pyexpat import model
from re import S, search
from django.contrib import admin
from .models import Contact, Categories, Stories, Tag, Images


class ImageAdmin(admin.TabularInline):
    model = Images
    fields = ('image', )

@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ['author', 'category', 'slug']
    list_filter = ['category']
    search_fields = ('author__username', )
    inlines = [ImageAdmin]

admin.site.register([Contact, Categories, Tag])
