from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pedido, Item
from virtus.api.serializers import PedidoSerializer, ItemSerializer


class PedidoView(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

