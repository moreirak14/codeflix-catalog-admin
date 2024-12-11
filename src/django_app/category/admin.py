from django.contrib import admin

from django_app.category.models import CategoryModel


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryModel, CategoryAdmin)
