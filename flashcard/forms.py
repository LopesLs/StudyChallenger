from django import forms

from .models import Flashcard


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["pergunta", "resposta", "categoria", "dificuldade"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pergunta"].widget.attrs.update({"class": "form-control"})
        self.fields["resposta"].widget.attrs.update({"class": "form-control"})
        self.fields["categoria"].widget.attrs.update({"class": "form-control"})
        self.fields["dificuldade"].widget.attrs.update({"class": "form-control"})
