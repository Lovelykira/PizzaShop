from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet, PizzaRecipecViewSet, IngredientViewSet, OrderViewSet, OrderItemPizzaViewSet, DrinkViewSet, \
    DrinkViewSet, OrderItemDrinkViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'recipes', PizzaRecipecViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitempizzas',OrderItemPizzaViewSet)
router.register(r'drinks', DrinkViewSet)
router.register(r'orderitemdrinks', OrderItemDrinkViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]