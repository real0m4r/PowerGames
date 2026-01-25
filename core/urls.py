from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/hello/', views.api_hello, name='api_hello'),
]
