from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from products.models import Product, Order
from products.serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Opcional: define permissão específica por view
    permission_classes = [IsAuthenticated] 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
