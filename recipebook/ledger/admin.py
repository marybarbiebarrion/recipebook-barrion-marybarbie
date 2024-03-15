from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ['name',]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)