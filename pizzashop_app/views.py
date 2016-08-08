from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Pizza, Order,OrderItemPizza
from pizzashop_app.forms import LoginForm, RegistrationForm, PizzaOrderForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


class PizzaListView(ListView):
    model = Pizza
    context_object_name = 'pizza_list'
    template_name = 'pizza_list.html'


class LoginView(FormView):
    template_name = 'log_in.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/')


class LogoutView(View, LoginRequiredMixin):
    redirect_field_name = '/login/'
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect('/')


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')


class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'pizza_details.html'


class BinView(ListView, LoginRequiredMixin):
    model = Order
    context_object_name = 'order_list'
    template_name = 'bin.html'
    redirect_field_name = '/login/'

    def get_queryset(self):
        order = Order.objects.filter(client=self.request.user, status='active')
        if order:
            order_item_pizza = OrderItemPizza.objects.filter(order=order)
            return order_item_pizza
        return False

    def get_context_data(self, **kwargs):
        context = super(BinView, self).get_context_data(**kwargs)
        order = Order.objects.filter(client=self.request.user, status='active')
        if order:
            order_item_pizza = OrderItemPizza.objects.filter(order=order)
            sum = 0
            for item in order_item_pizza:
                sum += item.total_cost
            context['total'] = sum
        return context


class BinCheckoutView(TemplateView, LoginRequiredMixin):
    template_name = 'bin.html'
    redirect_field_name = '/login/'

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(client=request.user, status='active')
        if order:
            order.status = 'closed'
            order.save()
        return HttpResponseRedirect('/bin/')


class BinChangeQuantityView(TemplateView,LoginRequiredMixin):
    template_name = 'bin.html'
    redirect_field_name = '/login/'

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(client=request.user, status='active')
        if order:
            order_item_pizza = OrderItemPizza.objects.get(order=order, pizza_id=request.POST['pizza_id'])
            order_item_pizza.quantity = request.POST['quantity']
            order_item_pizza.save()
        return HttpResponseRedirect('/bin/')


class PizzaOrderView(TemplateView, LoginRequiredMixin):
    redirect_field_name = '/login/'
    template_name = 'pizza_list.html'

    def post(self, request, *args, **kwargs):
        order = Order.objects.get_or_create(client=request.user, status='active')[0]

        OrderItemPizza.objects.create(order=order, pizza_id=request.POST['pizza_id'], quantity=int(request.POST['quantity']))
        order.save()
        return HttpResponseRedirect('/')

