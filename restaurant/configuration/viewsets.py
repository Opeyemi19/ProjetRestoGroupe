from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class AllFrontViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = AllFront.objects.all()
    serializer_class = AllFrontSerializer


class StepIndexViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = StepIndex.objects.all()
    serializer_class = StepIndexSerializer


class InfoViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class WorkingHoursViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer

class AboutViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = About.objects.all()
    serializer_class = AboutSerializer