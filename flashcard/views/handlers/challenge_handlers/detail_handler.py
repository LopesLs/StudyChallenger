from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from ....models import Desafio


class ChallengeDetailRequestHandler(LoginRequiredMixin, DetailView):
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
