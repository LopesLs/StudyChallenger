from django.urls import path

from . import views

urlpatterns = [
    path('apostila_create', views.NewApostilaRequestHandler.as_view(), name='apostila_create'),
    path('detail-apostila/<int:pk>', views.ApostilaDetailRequestHandler.as_view(), name='detail_apostila'),
]