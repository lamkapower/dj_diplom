from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['company_name', 'id', 'registration_data', 'edit_date', 'verify']
    # list_display_links = ['company_name']

    # search_fields = ['ogrn']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
