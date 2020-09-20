from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    # list_display = ['company_name', 'id', 'registration_data', 'edit_date', 'verify']
    # list_display_links = ['company_name']

    # search_fields = ['ogrn']

    class Meta:
        model = Review


admin.site.register(Review, ReviewAdmin)
