from django.test import TestCase

from catalogo.models import Categoria


class CategoriaPagesTests(TestCase):
    def test_home_redirects_to_categoria_list(self):
        response = self.client.get("/")

        self.assertRedirects(
            response, "/catalogo/categorias/", fetch_redirect_response=False
        )

    def test_categoria_list_page_loads(self):
        response = self.client.get("/catalogo/categorias/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "categoria_list.html")

    def test_categoria_form_page_loads(self):
        response = self.client.get("/catalogo/categorias/crear/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario.html")
        self.assertContains(response, 'name="nombre"')
        self.assertContains(response, 'name="descripcion"')

    def test_categoria_form_creates_categoria(self):
        response = self.client.post(
            "/catalogo/categorias/crear/",
            {"nombre": "Novela", "descripcion": "Libros de ficción"},
        )

        self.assertRedirects(response, "/catalogo/categorias/")
        self.assertTrue(
            Categoria.objects.filter(
                nombre="Novela", descripcion="Libros de ficción"
            ).exists()
        )
