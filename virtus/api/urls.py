from django.urls import path, include
from rest_framework import routers

from .views import PedidoView, ItemView

router = routers.DefaultRouter()
router.register(r'pedidos', PedidoView, base_name='pedidos')
router.register(r'itens', ItemView, base_name='itens')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]
