from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from main.models import Product


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class ProductTemplateView(TemplateView):
    template_name = 'main/products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        from itertools import zip_longest
        objs = Product.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))



# def index(request: HttpRequest):
#     return HttpResponse('<b>Hello</b>')




