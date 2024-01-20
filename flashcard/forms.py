from django import forms

from .models import Flashcard, Desafio


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["pergunta", "resposta", "categoria", "dificuldade"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pergunta"].widget.attrs.update({"class": "form-control"})
        self.fields["resposta"].widget.attrs.update({"class": "form-control limited-textarea"})
        self.fields["categoria"].widget.attrs.update({"class": "form-control"})
        self.fields["dificuldade"].widget.attrs.update({"class": "form-control"})


class DesafioForm(forms.ModelForm):
    class Meta:
        model = Desafio
        fields = ["titulo", "categoria", "dificuldade", "quantidade_perguntas"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({"class": "form-control"})
        self.fields["categoria"].widget.attrs.update({"class": "form-control"})
        self.fields["dificuldade"].widget.attrs.update({"class": "form-control"})
        self.fields["quantidade_perguntas"].widget.attrs.update({"class": "form-control"})
