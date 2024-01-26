from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from ....models import Desafio
from ...utils.global_utils import filter_by_user


class ChallengeDetailRequestHandler(LoginRequiredMixin, DetailView):
    """
    This class shows a challenge detail
    """
    
    model = Desafio
    template_name = "challenge/challenge_detail.html"
    context_object_name = "challenge"

    def get_context_data(self, **kwargs):
        """
        Send the number of hits, errors, missing and categories to the template
        """

        context = super().get_context_data(**kwargs)

        challenge = context["challenge"]

        context["acertos"] = challenge.flashcards.filter(
            respondido=True, acertou=True
        ).count()

        context["erros"] = challenge.flashcards.filter(
            respondido=True, acertou=False
        ).count()

        context["faltantes"] = challenge.flashcards.filter(respondido=False).count()

        context["categories"] = challenge.flashcards.all().values_list(
            "flashcard__categoria__nome", flat=True
        ).distinct()

        return context

    def get_queryset(self):
        """
        Filter challenges by the current user
        """

        queryset = super().get_queryset()
        return filter_by_user(queryset, self.request)
