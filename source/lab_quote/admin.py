from django.contrib import admin
from lab_quote.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at', 'author_name', 'author_email', 'rating', 'status']
    list_filter = ['author_name', 'created_at']
    search_fields = ['text', 'author_name']
    fields = ['text', 'created_at', 'author_name', 'author_email', 'rating', 'status']
    readonly_fields = ['created_at']


admin.site.register(Quote, QuoteAdmin)