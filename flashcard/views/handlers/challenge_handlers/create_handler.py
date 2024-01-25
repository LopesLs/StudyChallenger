from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from ....models import Flashcard, Desafio, FlashcardDesafio
from ....forms import DesafioForm


class ChallengeCreateRequestHandler(LoginRequiredMixin, CreateView):
    """
    This class creates a challenge
    """
    
    model = Desafio
    form_class = DesafioForm
    template_name = "challenge/challenge_create.html"
    success_url = reverse_lazy("challenge_list")

    def post(self, request, *args, **kwargs):
        """
        Create a challenge, flashcard_desafio and add flashcards to the challenge
        """

        # TODO: Refactor this method in soon

        form = self.get_form()
        form.instance.user = self.request.user

        if not form.is_valid():
            return redirect(reverse_lazy("challenge_list"))

        if (
            form.instance.quantidade_perguntas
            > Flashcard.objects.filter(
                user=self.request.user, dificuldade=form.instance.dificuldade
            ).count()
        ):
            messages.error(request, "Não há flashcards suficientes")

            return redirect(reverse_lazy("challenge_create"))

        desafio = Desafio(
            user=self.request.user,
            titulo=form.instance.titulo,
            quantidade_perguntas=form.instance.quantidade_perguntas,
            dificuldade=form.instance.dificuldade,
        )

        categorias = list(form.cleaned_data.get("categoria"))

        desafio.save()
        desafio.categoria.add(*categorias)

        flashcards = Flashcard.objects.filter(
            user=self.request.user,
            categoria_id__in=categorias,
            dificuldade=form.instance.dificuldade,
        ).order_by("?")

        flashcards = flashcards[: form.instance.quantidade_perguntas]

        flashcard_desafios = [
            FlashcardDesafio(flashcard=flashcard) for flashcard in flashcards
        ]

        FlashcardDesafio.objects.bulk_create(flashcard_desafios)

        desafio.flashcards.add(*flashcard_desafios)
        desafio.save()

        return redirect(reverse_lazy("challenge_detail", kwargs={"pk": desafio.pk}))
