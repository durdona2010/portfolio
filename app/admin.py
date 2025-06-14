from django.contrib import admin
from .models import Blog,Contact,Categories,BlogCategories

admin.site.register((Blog,Categories,BlogCategories))


    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('firstname','email','subject','message')
