from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    # list_display = ('title', 'created_at', 'updated_at', 'author')
    list_display = ('title', 'created_at', 'updated_at', 'author_name', 'content_length', 'thumbnail_image')
    ordering = ('created_at',)
    # ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        ("Auteur & Publication", {
            'fields': ('author', 'is_published', 'publication_date')
        }),
        ("Contenu", {
            'fields': ('title', 'content')
        }),
        ("Médias", {
            'fields': ('image',)
        })
    )


    def author_name(self, obj):
        if obj.author:
            return obj.author.first_name
        return '(Anonyme)'

    def content_length(self, obj):
        return len(obj.content)

    def thumbnail_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;"', obj.image.url);
        return '(Pas d\'image)'

    author_name.short_description = 'Auteur'
    thumbnail_image.short_description = 'Image'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)