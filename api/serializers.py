from rest_framework import serializers

from pizzashop_app.models import Pizza, PizzaRecipe, Ingredients, Order, OrderItemPizza


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
    recipe = PizzaRecipeSerializer()

    class Meta:
        model = Pizza
        fields = ('id', 'recipe', 'weight', 'diameter', 'price')


class OrderItemPizzaSerializer(serializers.ModelSerializer):
    #order = OrderSerializer()
    pizza = PizzaSerializer()

    class Meta:
        model = OrderItemPizza
        fields = ('id', 'order', 'pizza', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    pizzas = OrderItemPizzaSerializer(many=True, source='order_pizzas')

    class Meta:
        model = Order
        fields = ('id', 'client', 'date', 'pizzas', 'status')












