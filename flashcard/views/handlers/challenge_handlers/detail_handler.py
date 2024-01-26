from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from ....models import Desafio
from ...utils.global_utils import filter_by_user
from ...utils.challenge_utils import update_challenge_context_data


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

        context.update(update_challenge_context_data(challenge))

        return context

    def get_queryset(self):
        """
        Filter challenges by the current user
        """

        queryset = super().get_queryset()
        return filter_by_user(queryset, self.request)
