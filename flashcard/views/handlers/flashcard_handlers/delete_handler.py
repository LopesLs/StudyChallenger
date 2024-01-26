from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from ....models import Flashcard
from ...utils.global_utils import filter_by_user


class FlashcardDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    """
    Delete a flashcard
    """

    model = Flashcard
    template_name = "flashcard/flashcard_delete.html"
    success_url = reverse_lazy("list-flashcards")

    def get_queryset(self):
        """
        Return only flashcards from the current user
        """

        queryset = super().get_queryset()
        
        return filter_by_user(queryset, self.request)
