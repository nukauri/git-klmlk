from django.urls import path
from accomodation.api import view as api_views

urlpatterns = [
    path('api/',api_views.AccomodationListCreateAPIView.as_view(),name='konaklamalist')
]