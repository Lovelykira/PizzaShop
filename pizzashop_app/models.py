from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PizzaRecipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    recipe = models.ForeignKey(PizzaRecipe)
    weight = models.PositiveIntegerField()
    diameter = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.recipe.name, self.diameter, self.price)

    def get_absolute_url(self):
        return reverse('pizza_details', kwargs={'pk': self.pk})


class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.FloatField()
    in_stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    pizzas = models.ManyToManyField(Pizza, through='OrderItemPizza')
    drinks = models.ManyToManyField(Drink, through='OrderItemDrink')

    CLOSED = 'closed'
    ACTIVE = 'active'
    STATUS_CHOICES = ((CLOSED, 'closed'),(ACTIVE, 'active'))
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return "Order {}".format(self.pk)


class OrderItemPizza(models.Model):
    order = models.ForeignKey(Order)
    pizza = models.ForeignKey(Pizza)
    quantity = models.PositiveIntegerField()

    def _get_total(self):
        return self.pizza.price * self.quantity
    total_cost = property(_get_total)


class OrderItemDrink(models.Model):
    order = models.ForeignKey(Order)
    drink = models.ForeignKey(Drink)
    quantity = models.PositiveIntegerField()

    def _get_total(self):
        return self.product.price * self.quantity
    total_cost = property(_get_total)
