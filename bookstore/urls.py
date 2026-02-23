from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token # Import para gerar o token
from products import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'order', views.OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Rota para obter o token enviando username e password
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]
