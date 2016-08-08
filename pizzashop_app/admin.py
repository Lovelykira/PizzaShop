from django.contrib import admin
from .models import *


class IngredientsAdmin(admin.ModelAdmin):    pass


class PizzaRecipeAdmin(admin.ModelAdmin):pass


class PizzaAdmin(admin.ModelAdmin):pass


class DrinkAdmin(admin.ModelAdmin):pass



class OrderItemPizzaAdmin(admin.TabularInline):
    model = OrderItemPizza

class OrderItemDrinkAdmin(admin.TabularInline):pass



class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemPizzaAdmin,)


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(PizzaRecipe, PizzaRecipeAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Order, OrderAdmin)