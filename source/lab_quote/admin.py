from django.contrib import admin
from lab_quote.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'created_at', 'author_name', 'author_email', 'rating', 'status']
    list_filter = ['created_at', 'author_name']
    search_fields = ['text', 'author_name']
    fields = ['pk', 'text', 'created_at', 'author_name', 'author_email', 'rating', 'status']
    readonly_fields = ['created_at']


admin.site.register(Quote, QuoteAdmin)

