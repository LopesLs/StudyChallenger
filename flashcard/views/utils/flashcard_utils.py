from django.shortcuts import redirect
from django.urls import reverse_lazy

from ...models import FlashcardDesafio, Desafio


def AwnserFlashcardRequestHandler(request, pk):
    flashcard_desafio = FlashcardDesafio.objects.get(id=pk)

    if flashcard_desafio.flashcard.user != request.user:
        return redirect(reverse_lazy("list-flashcards"))

    flashcard_desafio.respondido = True
    flashcard_desafio.acertou = True if request.GET.get("acertou") == "1" else False
    flashcard_desafio.save()

    challenge = Desafio.objects.get(id=request.GET.get("desafio_id"))
    challenge_flashcards = challenge.flashcards.all().count()
    challenge_flashcards_respondidos = challenge.flashcards.filter(
        respondido=True
    ).count()

    if challenge_flashcards_respondidos == challenge_flashcards:
        challenge.status = True
        challenge.save()

    return redirect(
        reverse_lazy("challenge_detail", kwargs={"pk": request.GET.get("desafio_id")})
    )
