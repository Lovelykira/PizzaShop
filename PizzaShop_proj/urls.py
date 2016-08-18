"""PizzaShop_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from pizzashop_app.views import PizzaListView, LoginView, LogoutView, RegisterView, PizzaDetailView, BinView, \
    PizzaOrderView,BinCheckoutView, BinChangeQuantityView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls') ),
    url(r'^accounts/profile/$',  RedirectView.as_view(url='/', permanent=False), name='index'),
    url(r'^$', PizzaListView.as_view(), name='pizza_list'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^(?P<pk>\d+)/$', view=PizzaDetailView.as_view(), name='pizza_details'),
    url(r'^bin/$', BinView.as_view()),
    url(r'^bin/checkout/$', BinCheckoutView.as_view()),
    url(r'^bin/change_quantity/$', BinChangeQuantityView.as_view()),
    url(r'^pizza/(?P<pk>\d+)/order/$', view=PizzaOrderView.as_view(), name='pizza_order'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()