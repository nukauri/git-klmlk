from django.urls import path

from . import views
from account.api import views as api_views

app_name='account'

urlpatterns = [
    path('new/',views.new,  name='new'),
    path('<int:pk>',views.detail,name='detail'),
    path('api/',views.AccountListAPIView.as_view()),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]