from django.urls import path

from . import views

urlpatterns = [
    path('new-apostila', views.NewApostilaRequestHandler.as_view(), name='new_apostila'),
    path('detail-apostila/<int:pk>', views.ApostilaDetailRequestHandler.as_view(), name='detail_apostila'),
]