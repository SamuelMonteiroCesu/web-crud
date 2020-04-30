from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste, name='liste'),
    path('relat/<int:id>', views.listeViews, name='liste-views'),
    path('addProduto/', views.novoProduto, name='novo-produto'),
    path('editProduto/<int:id>', views.editProduto, name='edit-produto'),
    path('deleteProduto/<int:id>', views.deleteProduto, name='delete-Produto'),
]