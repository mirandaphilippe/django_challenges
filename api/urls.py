
from django.urls import path, include, register_converter
from . import views, converters
from rest_framework import routers

register_converter(converters.DataConverter, 'date')

urlpatterns = [
    path('order/items/<date:begin>/<date:final>/', views.orderItemByDate),
]
