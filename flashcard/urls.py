from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlashcardRequestHandler.as_view(), name='list-flashcards'),
    path('new-flashcard/', views.NewFlashcardRequestHandler.as_view(), name='new-flashcard'),
    path('del-flashcard/<int:pk>', views.DelFlashcardRequestHandler.as_view(), name='del-flashcard'),
]