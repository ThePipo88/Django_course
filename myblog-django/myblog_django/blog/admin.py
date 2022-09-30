from django.contrib import admin

#Models
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'title','desc','created')
    list_display_links = ('title','title',)
    list_filter = ('created','update')
    search_fields = ('title','desc')
    
    readonly_fields = ('created','update')