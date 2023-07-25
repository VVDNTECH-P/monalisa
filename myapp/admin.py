from django.contrib import admin
from .models import admin_post , comments,Information
# Register your models here.
@admin.register(admin_post)
class admin_postAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'desc' , 'image']

@admin.register(comments)
class admin_coments(admin.ModelAdmin):
    list_display = ['user' , 'user_id' , 'message']

@admin.register(Information)
class admin_coments(admin.ModelAdmin):
    list_display = ['title' , 'date' ]