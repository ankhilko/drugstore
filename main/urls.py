from django.urls import path
from .views import IndexTemplateView, ProductListView, AboutTemplateView, WorkScheduleListView, ProductApiView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('store/', WorkScheduleListView.as_view(), name='store'),
    path('api/v1/products/', ProductApiView.as_view(), name='products_api'),          # создали энд поинт для АПИ

]
