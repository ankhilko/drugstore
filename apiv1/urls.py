from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet


api_router = SimpleRouter()
api_router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
    # path('products/', ProductViewSet.as_view({'get': 'list'},)),        # своя апишка на джанге
    path('login/', obtain_auth_token),
]




# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # только руками (((
