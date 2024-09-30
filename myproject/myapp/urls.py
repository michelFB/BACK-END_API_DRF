# myapp/urls.py
from django.urls import path
from .views import item_list
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('items-page/', item_list, name='item_list'),
    path('', include(router.urls)),
]
