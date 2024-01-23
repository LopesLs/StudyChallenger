from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib import messages

from ..models import Flashcard, Categoria, Desafio, FlashcardDesafio
from ..forms import DesafioForm


class NewChallengeRequestHandler(LoginRequiredMixin, CreateView):
    model = Desafio
    form_class = DesafioForm
    template_name = "challenge/challenge_create.html"
    success_url = reverse_lazy("challenge_list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.user = self.request.user

        if not form.is_valid():
            return redirect(reverse_lazy("challenge_list"))

        if form.instance.quantidade_perguntas > Flashcard.objects.filter(
                user=self.request.user, dificuldade=form.instance.dificuldade
            ).count():
            
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


class ListChallengeRequestHandler(LoginRequiredMixin, ListView):
    model = Desafio
    template_name = "challenge/challenge_list.html"
    context_object_name = "challenges"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        difficulty = self.request.GET.get("difficulty")

        if category:
            queryset = queryset.filter(categoria__id=category)

        if difficulty:
            queryset = queryset.filter(dificuldade=difficulty)

        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categoria.objects.all()
        context["dificulties"] = Flashcard.DIFICULDADE_CHOICES
        return context


class DetailChallengeRequestHandler(LoginRequiredMixin, DetailView):
    model = Desafio
    template_name = "challenge/challenge_detail.html"
    context_object_name = "challenge"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        challenge = context["challenge"]

        context["acertos"] = challenge.flashcards.filter(
            respondido=True, acertou=True
        ).count()

        context["erros"] = challenge.flashcards.filter(
            respondido=True, acertou=False
        ).count()

        context["faltantes"] = challenge.flashcards.filter(respondido=False).count()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DelChallengeRequestHandler(LoginRequiredMixin, DeleteView):
    model = Desafio
    template_name = "flashcard/flashcard_delete.html"
    success_url = reverse_lazy("challenge_list")


def RelatoryChallengeRequestHandler(request, pk):
    challenge = Desafio.objects.get(id=pk)

    if challenge.user != request.user:
        return HttpResponseForbidden()

    acertos = challenge.flashcards.filter(respondido=True, acertou=True).count()
    erros = challenge.flashcards.filter(respondido=True, acertou=False).count()
    categories = challenge.categoria.all()
    name_categories = [category.nome for category in categories]

    resultados_por_categoria = {}

    for category in categories:
        resultados_por_categoria[f"{category}"] = {
            "acertos": (
                challenge.flashcards.filter(flashcard__categoria=category)
                .filter(acertou=True)
                .count()
            )
        }
        resultados_por_categoria[f"{category}"]["erros"] = (
            challenge.flashcards.filter(flashcard__categoria=category)
            .filter(acertou=False)
            .count()
        )

    acertos_por_categoria = [
        resultados_por_categoria[category]["acertos"]
        for category in resultados_por_categoria
    ]

    return render(
        request,
        "challenge-relatory.html",
        {
            "challenge": challenge,
            "acertos": acertos,
            "erros": erros,
            "acertos_por_categoria": acertos_por_categoria,
            "resultados_por_categoria": resultados_por_categoria,
            "categories": name_categories,
        },
    )
