from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','category', 'show',
    ordering = '-id', 
    list_filter = 'created_date',
    search_fields = 'first_name',
    list_per_page = 25
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', 