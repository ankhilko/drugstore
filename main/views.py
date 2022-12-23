from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, ListView

from main.models import Product, WorkSchedule


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class ProductListView(ListView):
    template_name = 'main/products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        from itertools import zip_longest
        objs = Product.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))


class AboutTemplateView(TemplateView):
    template_name = 'main/about.html'
    context_object_name = 'about'


class WorkScheduleListView(ListView):
    template_name = 'main/store.html'
    model = WorkSchedule
    context_object_name = 'week'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['weekday'] = datetime.today().isoweekday()
        return context




# def index(request: HttpRequest):
#     return HttpResponse('<b>Hello</b>')




