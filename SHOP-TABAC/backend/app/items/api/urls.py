from django.urls import path, include
from items.api.views import *
urlpatterns = [
    path('list/', ItemListAPI.as_view(), name="item-list"),
    path('list/<int:id>/', ItemDetailAPI.as_view(), name="item-detail"),

    path('categories/', CategoryListAPI.as_view(),name='category-list'),#+
    path('categories/<slug:slug>/', CategoryDetailAPI.as_view(),name='category-detail'),#+
    path('categories/items/<slug:slug>/',CategoryItemsListAPI.as_view())
]
