# myapp/views.py
from django.shortcuts import render
from .models import Item
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Item
from .serializers import ItemSerializer

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    name = "Item-list"
    
    
# class ApiRoot(generics.GenericAPIView):
#     name = "api-root"
#     def get(self, request, *args, **kwargs):
#         return Response(
#             {
#                 "drone": reverse("Item-list", request=request),
#             }
#         )