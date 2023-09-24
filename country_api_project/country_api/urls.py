from django.urls import path
from .views import Auth
from .views import CountryDetail, CountryList

urlpatterns = [
    path('auth/', YourAuthView.as_view(), name='auth'),  # Implement authentication as needed
    path('country/<str:country_name>/', CountryDetail.as_view(), name='country-detail'),
    path('countries/', CountryList.as_view(), name='country-list'),
]
urlpatterns = [
    path('auth/', Auth.as_view(), name='auth'),
    # ... Other URL patterns for your API
]
