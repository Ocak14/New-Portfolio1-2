from django.contrib import admin
from .models import Contact,Portfolio,Blog,Comment,Category,Gallery,Books
from django.utils.html import format_html
# Register your models here.


admin.site.register((Comment,Category,Blog,Books))


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    readonly_fields = ['id']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    readonly_fields = ['id']

from django.shortcuts import render
from .models import Blog 
def blog_view(request):
    
    blogs = Blog.objects.all()
  
    return render(request, 'blog.html', {'blogs': blogs})



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'created_date')
    readonly_fields = ['id']

    def img(self, obj):
        return format_html(
            '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
            obj.image.url
        )
    




    