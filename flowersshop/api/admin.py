from django.contrib import admin

from .models import Flower, Extra, Bucket

admin.site.site_header = "Лох - цветочный"


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description", "price")


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description", "price")

@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description", "price")
