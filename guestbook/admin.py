from django.contrib import admin
from .models import text

class textAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title_text']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    list_filter = ['pub_date']


admin.site.register(text, textAdmin)
