from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/adv_metrics', views.adv_metrics, name='adv_metrics'),
]