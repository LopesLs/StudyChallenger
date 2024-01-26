from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from ....models import Desafio


class ChallengeDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    """
    This class deletes a flashcard
    """
    
    model = Desafio
    template_name = "flashcard/flashcard_delete.html"
    success_url = reverse_lazy("challenge_list")
