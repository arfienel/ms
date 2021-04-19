from django.contrib import admin
from.models import Comment,News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date')


admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
# Register your models here.
