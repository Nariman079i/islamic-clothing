from django.contrib import admin
from .models import *
# Register your models here.

class ClothingModel(admin.ModelAdmin):
    list_display = ('title' , 'type_cl' , 'color' , 'price' , 'on_view_post')
    list_display_links = ('title',)
    list_editable = ( 'type_cl' , 'color' , 'price' , 'on_view_post')

admin.site.register(Types)
admin.site.register(Clothing , ClothingModel )