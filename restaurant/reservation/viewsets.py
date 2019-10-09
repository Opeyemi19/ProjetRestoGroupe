from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class TableViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class JourViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Jour.objects.filter(status=True)
    serializer_class = JourSerializer


class HeureViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Heure.objects.filter(status=True)
    serializer_class = HeureSerializer


class PersonViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Person.objects.filter(status=True)
    serializer_class = PersonSerializer


class TableMessageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = TableMessage.objects.all()
    serializer_class = TableMessageSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer