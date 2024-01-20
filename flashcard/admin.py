from django.contrib import admin

from .models import Flashcard, Categoria, Desafio, FlashcardDesafio

for model in [Flashcard, Categoria, Desafio, FlashcardDesafio]:
    admin.site.register(model)
