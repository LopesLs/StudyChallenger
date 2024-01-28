from django.test import TestCase

from ..models import Categoria


class CategoriaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Categoria.objects.create(nome="Categoria 1")

    def test_nome_label(self):
        categoria = Categoria.objects.get(id=1)
        field_label = categoria._meta.get_field("nome").verbose_name
        self.assertEquals(field_label, "nome")

    def test_instance_creation(self):
        category = Categoria.objects.get(id=1)
        self.assertTrue(isinstance(category, Categoria))
