from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated # <--- Verifique se importou isso
from .models import Produto, Order
from .serializers import ProdutoSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny] # <--- ESSA LINHA É A TRAVA

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # <--- ESSA LINHA É A TRAVA
