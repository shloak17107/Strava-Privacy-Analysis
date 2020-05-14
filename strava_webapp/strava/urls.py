from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home-view'),
    path('stravaUser/', views.stravaAuthentication, name='strava-authentication'),
    path('sampleData/', views.sampleData, name='sample-data'),
]