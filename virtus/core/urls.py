from django.urls import path
from .views import dashboard, edit

app_name = 'core'
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('editar/<slug:slug>/', edit, name="edit-cliente"),

]
