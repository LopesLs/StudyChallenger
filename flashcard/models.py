from django.contrib.auth.models import User
from django.db import models


class Flashcard(models.Model):
    DIFICULDADE_CHOICES = (("D", "Difícil"), ("M", "Médio"), ("F", "Fácil"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()
    categoria = models.ForeignKey("Categoria", on_delete=models.DO_NOTHING)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)
    
    @property
    def css_difficulty(self):
        if self.dificuldade == "F":
            return ["success", "Fácil"]
        elif self.dificuldade == "M":
            return ["warning", "Médio"]
        elif self.dificuldade == "D":
            return ["danger", "Difícil"]

    def delete(self, *args, **kwargs):
        desafios = Desafio.objects.filter(flashcards__flashcard=self)

        for desafio in desafios:
            print(desafio.flashcards.count())
            if desafio.flashcards.count() <= 1:
                raise Exception("Não é possível excluir o flashcard, pois ele está sendo utilizado em um desafio.")
        
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.pergunta


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class FlashcardDesafio(models.Model):
    flashcard = models.ForeignKey("Flashcard", on_delete=models.CASCADE)
    respondido = models.BooleanField(default=False)
    acertou = models.BooleanField(default=False)

    def __str__(self):
        return self.flashcard.pergunta


class Desafio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
    quantidade_perguntas = models.IntegerField()
    dificuldade = models.CharField(max_length=1, choices=Flashcard.DIFICULDADE_CHOICES)
    flashcards = models.ManyToManyField(FlashcardDesafio)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
