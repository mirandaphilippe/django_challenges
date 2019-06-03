from django.shortcuts import render
from rest_framework import viewsets
from . import converters
from .models import OrderItem
from .serializers import OrderItemSerializer
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests


convert = converters.DataConverter()
weatherKey = 'd3db98f9254d535bd00b5a607ff9db7e'
clientId = 'c8288de2857441ffaae2abd58380c684'

def orderItemByDate(req, begin,final):
    try:
        res = requests.get('http://www.mocky.io/v2/5817803a1000007d01cc7fc9')
        items = res.json()
        filteredItems = []

        if res.status_code == 200:
            for item in items:
                itemDate = convert.from_json(item['date'])
                if itemDate >= begin and itemDate <= final:
                  filteredItems.append(item)
                   
        return JsonResponse(filteredItems, safe = False)
    
    except Exception as e:
        return e


