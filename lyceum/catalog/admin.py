from django.contrib import admin

import catalog.models

__all__ = []

admin.site.register(catalog.models.Category)
admin.site.register(catalog.models.Tag)


class MainImage(admin.TabularInline):
    model = catalog.models.MainImage
    fields = ('image',)


class Images(admin.TabularInline):
    model = catalog.models.Images
    fields = ('image',)


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.image_tmb,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)

    inlines = (
        MainImage,
        Images,
    )
