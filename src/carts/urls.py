from django.urls import re_path

from .views import cart_home, cart_update, checkout_done_view, checkout_home

urlpatterns = [
    re_path(r'^$', cart_home, name='home'),
    re_path(r'^checkout/success/$', checkout_done_view, name='success'),
    re_path(r'^checkout/$', checkout_home, name='checkout'),
    re_path(r'^update/$', cart_update, name='update'),
]