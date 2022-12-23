from django.contrib import admin

from .models import Category, Product, WorkSchedule
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_filter = ('name',)
    ordering = ('is_published', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    ordering = ('is_published', 'name')
    search_fields = ('name',)


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'opening_time', 'closing_time')
    search_fields = ('week_day',)

