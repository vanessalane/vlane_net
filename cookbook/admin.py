from django.contrib import admin

from .models import Recipe, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'yield_count', 'yield_units', 'prep_time', 
            'cook_time', 'time_units', 'instructions']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [IngredientInline]

    list_display = ('title', 'pub_date')
    search_fields = ['title']


admin.site.register(Recipe, RecipeAdmin)
