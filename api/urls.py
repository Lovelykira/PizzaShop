from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet, PizzaRecipecViewSet, IngredientViewSet, OrderViewSet, OrderItemPizzaViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'recipes', PizzaRecipecViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitempizzas',OrderItemPizzaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]