from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ....models import Flashcard
from ....forms import FlashcardForm


class FlashcardCreateRequestHandler(LoginRequiredMixin, CreateView):
    """
    Create a new flashcard
    """

    model = Flashcard
    form_class = FlashcardForm
    template_name = "flashcard/flashcard_create.html"
    success_url = reverse_lazy("list-flashcards")

    def form_valid(self, form):
        """
        Set the current user as the flashcard's user before saving
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
