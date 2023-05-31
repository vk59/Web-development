from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from weather.models import User, Country, Town
from weather.serializers import UserSerializer, TownSerializer, CountrySerializer


class UserPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class UserAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission]

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user


class CountriesAPIView(ListAPIView, CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPagination
    filter_backends = []
    filter_fields = ['continent']
    search_fields = ['name']


class TownsAPIView(ListAPIView, CreateAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    pagination_class = PageNumberPagination
    filter_backends = []
    filter_fields = ['country']
    search_fields = ['name']
