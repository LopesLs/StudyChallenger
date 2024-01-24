from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlashcardListRequestHandler.as_view(), name='list-flashcards'),
    
    path('flashcard_create/', views.FlashcardCreateRequestHandler.as_view(), name='flashcard_create'),
    path('flashcard_delete/<int:pk>', views.FlashcardDeleteRequestHandler.as_view(), name='flashcard_delete'),
    path('awnser-flashcard/<int:pk>', views.AwnserFlashcardRequestHandler, name='awnser-flashcard'),
    
    path('challenge_create/', views.ChallengeCreateRequestHandler.as_view(), name='challenge_create'),
    path('del-challenge/<int:pk>', views.ChallengeDeleteRequestHandler.as_view(), name='del-challenge'),
    path('challenge_list/', views.ChallengeListRequestHandler.as_view(), name='challenge_list'),
    path('challenge_detail/<int:pk>', views.ChallengeDetailRequestHandler.as_view(), name='challenge_detail'),

    path('challenge-relatory/<int:pk>', views.RelatoryChallengeRequestHandler, name='challenge-relatory'),
]