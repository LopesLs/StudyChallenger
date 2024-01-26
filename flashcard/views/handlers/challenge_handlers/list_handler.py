from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ....models import Desafio, Categoria, Flashcard
from ...utils.global_utils import filter_by_user, filter_by_fields


class ChallengeListRequestHandler(LoginRequiredMixin, ListView):
    model = Desafio
    template_name = "challenge/challenge_list.html"
    context_object_name = "challenges"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        difficulty = self.request.GET.get("difficulty")

        queryset = filter_by_user(queryset, self.request)

        queryset = filter_by_fields(queryset, category, difficulty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categoria.objects.all()
        context["dificulties"] = Flashcard.DIFICULDADE_CHOICES
        return context
