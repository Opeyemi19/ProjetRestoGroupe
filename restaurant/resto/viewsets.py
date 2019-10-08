from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *



class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class MenuViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SpecialiteViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
