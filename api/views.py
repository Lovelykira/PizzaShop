from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from pizzashop_app.models import Pizza, PizzaRecipe,Ingredients, Order, OrderItemPizza
from api.serializers import PizzaSerializer, PizzaRecipeSerializer, IngredientSerializer, OrderSerializer, OrderItemPizzaSerializer



class UserList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer



class PizzaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaRecipecViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = PizzaRecipe.objects.all()
    serializer_class = PizzaRecipeSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemPizzaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = OrderItemPizza.objects.all()
    serializer_class = OrderItemPizzaSerializer

