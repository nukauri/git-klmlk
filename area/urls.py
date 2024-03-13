from django.urls import path
from area.api import views as api_views

urlpatterns = [
    path('api/',api_views.AreaListAPIView.as_view(),name='Arealist'),
    path('api/address/',api_views.AddressListAPIView.as_view(),name='Addresslist')
]