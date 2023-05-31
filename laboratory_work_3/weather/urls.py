from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from weather.views import UserAPIView, CountriesAPIView, TownsAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('user/', UserAPIView.as_view()),
    path('towns/', TownsAPIView.as_view()),
    path('countries/', CountriesAPIView.as_view()),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
