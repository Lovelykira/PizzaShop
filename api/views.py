from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from pizzashop_app.models import Pizza, PizzaRecipe,Ingredients, Order, OrderItemPizza, Drink, OrderItemDrink
from api.serializers import PizzaSerializer, PizzaRecipeSerializer, IngredientSerializer, OrderSerializer, OrderItemPizzaSerializer,\
                            DrinkSerializer, OrderItemDrinkSerializer


class UserList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer



class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaRecipecViewSet(viewsets.ModelViewSet):
    queryset = PizzaRecipe.objects.all()
    serializer_class = PizzaRecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemPizzaViewSet(viewsets.ModelViewSet):
    queryset = OrderItemPizza.objects.all()
    serializer_class = OrderItemPizzaSerializer


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class OrderItemDrinkViewSet(viewsets.ModelViewSet):
    queryset = OrderItemDrink.objects.all()
    serializer_class = OrderItemDrinkSerializer
