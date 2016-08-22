from django import forms

from rest_framework import serializers

from pizzashop_app.models import Pizza, PizzaRecipe, Ingredients, Order, OrderItemPizza, Drink


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id','name',)


class PizzaRecipeSerializer(serializers.ModelSerializer):
    #ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredients.objects.all())
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = PizzaRecipe
        fields = ('id', 'name', 'image', 'description', 'ingredients')


class PizzaSerializer(serializers.ModelSerializer):
 #   recipe = PizzaRecipeSerializer()

    class Meta:
        model = Pizza
        fields = ('id', 'recipe', 'weight', 'diameter', 'price')
        widgets = {
            'recipe': forms.ModelChoiceField(queryset=PizzaRecipe.objects.all(), to_field_name="name")
        }


class OrderItemPizzaSerializer(serializers.ModelSerializer):
    #order = OrderSerializer()
    pizza = PizzaSerializer()

    class Meta:
        model = OrderItemPizza
        fields = ('id', 'order', 'pizza', 'quantity')


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'image', 'price', 'in_stock', 'description')


class OrderItemDrinkSerializer(serializers.ModelSerializer):
    #order = OrderSerializer()
    drink = DrinkSerializer()

    class Meta:
        model = OrderItemPizza
        fields = ('id', 'order', 'drink', 'quantity')
        widgets = {
            'drink' : forms.ModelChoiceField(queryset=Drink.objects.all(), to_field_name="name")
        }


class OrderSerializer(serializers.ModelSerializer):
    pizzas = OrderItemPizzaSerializer(many=True, source='order_pizzas')
    drinks = OrderItemDrinkSerializer(many=True, source='order_drinks')

    class Meta:
        model = Order
        fields = ('id', 'client', 'date', 'pizzas', 'drinks', 'status')













