from django.shortcuts import render
from django.http import HttpResponseForbidden

from ...models import Desafio


def RelatoryChallengeRequestHandler(request, pk):
    """
    Show a challenge relatory based on the user's answers
    """

    # TODO: Refactor this function

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
        "challenge/challenge_relatory.html",
        {
            "challenge": challenge,
            "acertos": acertos,
            "erros": erros,
            "acertos_por_categoria": acertos_por_categoria,
            "resultados_por_categoria": resultados_por_categoria,
            "categories": name_categories,
        },
    )


def update_challenge_context_data(challenge):
    """
    Get the number of hits, errors, missing and categories
    """

    context = {}

    context["acertos"] = challenge.flashcards.filter(
        respondido=True, acertou=True
    ).count()

    context["erros"] = challenge.flashcards.filter(
        respondido=True, acertou=False
    ).count()

    context["faltantes"] = challenge.flashcards.filter(respondido=False).count()

    context["categories"] = (
        challenge.flashcards.all()
        .values_list("flashcard__categoria__nome", flat=True)
        .distinct()
    )

    return context
