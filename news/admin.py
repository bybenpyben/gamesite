from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(Articles, ArticlesAdmin)
