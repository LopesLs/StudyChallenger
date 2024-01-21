from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlashcardRequestHandler.as_view(), name='list-flashcards'),
    
    path('flashcard_create/', views.NewFlashcardRequestHandler.as_view(), name='flashcard_create'),
    path('flashcard_delete/<int:pk>', views.DelFlashcardRequestHandler.as_view(), name='flashcard_delete'),
    path('awnser-flashcard/<int:pk>', views.AwnserFlashcardRequestHandler, name='awnser-flashcard'),
    
    path('new-challenge/', views.NewChallengeRequestHandler.as_view(), name='new-challenge'),
    path('del-challenge/<int:pk>', views.DelChallengeRequestHandler.as_view(), name='del-challenge'),
    path('challenge_list/', views.ListChallengeRequestHandler.as_view(), name='challenge_list'),
    path('challenge_detail/<int:pk>', views.DetailChallengeRequestHandler.as_view(), name='challenge_detail'),

    path('challenge-relatory/<int:pk>', views.RelatoryChallengeRequestHandler, name='challenge-relatory'),
]