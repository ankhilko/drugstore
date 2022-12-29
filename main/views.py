from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, ListView

from main.models import Product, WorkSchedule
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class ProductListView(LoginRequiredMixin, ListView):
    login_url = '/signin/'
    template_name = 'main/products.html'
    model = Product
    context_object_name = 'products'

    # def get_queryset(self):
    #     from itertools import zip_longest
    #     objs = Product.objects.filter(is_published=True)
    #     objs = iter(objs)
    #     return list(zip_longest(objs, objs))


from django.utils.translation import gettext as _
# {% load i18n %}
from django.utils.translation import ngettext


class AboutTemplateView(TemplateView):
    template_name = 'main/about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['heading'] = _('About us')       # любое форматирование но не f-string
        context['subheading'] = _('Our coffee')



class WorkScheduleListView(ListView):
    template_name = 'main/store.html'
    model = WorkSchedule
    context_object_name = 'week'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['weekday'] = datetime.today().isoweekday()
    #     return context




# def index(request: HttpRequest):
#     return HttpResponse('<b>Hello</b>')




