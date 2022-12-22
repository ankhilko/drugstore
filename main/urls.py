from django.urls import path
from .views import IndexTemplateView, ProductTemplateView
# from .views import AboutTemplateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products', ProductTemplateView.as_view(), name='products'),
    # path('about', AboutTemplateView.as_view(), name='about'),

]