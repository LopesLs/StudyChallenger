from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from ..models import Flashcard, Categoria, Desafio, FlashcardDesafio
from ..forms import FlashcardForm


class FlashcardRequestHandler(LoginRequiredMixin, ListView):
    model = Flashcard
    template_name = "flashcard/flashcard_list.html"
    context_object_name = "flashcards"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categoria.objects.all()
        context["dificulties"] = Flashcard.DIFICULDADE_CHOICES
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        difficulty = self.request.GET.get("dificulty")

        if category:
            queryset = queryset.filter(categoria__id=category)

        if difficulty:
            queryset = queryset.filter(dificuldade=difficulty)

        return queryset


class NewFlashcardRequestHandler(LoginRequiredMixin, CreateView):
    model = Flashcard
    form_class = FlashcardForm
    template_name = "flashcard/flashcard_create.html"
    success_url = reverse_lazy("list-flashcards")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DelFlashcardRequestHandler(LoginRequiredMixin, DeleteView):
    model = Flashcard
    template_name = "flashcard/flashcard_delete.html"
    success_url = reverse_lazy("list-flashcards")


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
