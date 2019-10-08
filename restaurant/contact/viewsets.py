from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class MessageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SouscriptionViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer