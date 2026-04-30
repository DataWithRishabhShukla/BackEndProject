from django.contrib import admin
from menu.models import Category ,MenuItem

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name","description","price","is_available","category"]