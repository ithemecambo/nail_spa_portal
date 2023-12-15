from django.contrib import admin
from shop.forms import *
from shop.models import *


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceCreateForm
    model = Service
    list_select_related = ['parent']
    list_display = ['service_photo', 'service_name', 'service_price', 'status']
    list_display_links = ['service_photo', 'service_name']
    list_filter = ['created_at', 'status']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 10
    save_on_top = True


class BusinessHourLevelInlineAdmin(admin.TabularInline):
    form = BusinessHourCreateForm
    model = BusinessHour
    extra = 0


class GalleryLevelInlineAdmin(admin.TabularInline):
    form = GalleryCreateForm
    model = Gallery
    extra = 0


class PromotionLevelInlineAdmin(admin.StackedInline):
    form = PromotionCreateForm
    model = Promotion
    extra = 0


class ShopAdmin(admin.ModelAdmin):
    form = ShopCreateForm
    model = Shop
    list_display = [
        'shop_logo_photo',
        'shop_name',
        'tel',
        'email',
        'website',
    ]

    list_display_links = [
        'shop_logo_photo',
        'shop_name',
        'tel',
        'email',
    ]

    list_filter = [
        'created_at',
        'status'
    ]

    search_fields = [
        'shop_name',
        'tel',
        'email',
        'website',
        'address'
    ]

    inlines = [
        PromotionLevelInlineAdmin,
        BusinessHourLevelInlineAdmin,
        GalleryLevelInlineAdmin
    ]

    ordering = ['shop_name']
    list_per_page = 10


admin.site.register(Service, ServiceAdmin)
admin.site.register(Shop, ShopAdmin)
