from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('resume/', views.ResumeView, name='resume'),
    path('vlpottery/', views.PotteryView, name='pottery'),
]
