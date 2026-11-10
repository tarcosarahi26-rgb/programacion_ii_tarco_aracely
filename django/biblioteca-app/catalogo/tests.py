from django.test import TestCase

from catalogo.models import Categoria, Libro


class CategoriaPagesTests(TestCase):
    def test_home_page_loads_with_main_navigation(self):
        for url in ("/", "/catalogo/catalogo/"):
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, "home.html")
                self.assertContains(response, "Menú Principal")
                self.assertContains(response, "/catalogo/libros/")
                self.assertContains(response, "/catalogo/categorias/")

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

    def test_categoria_edit_page_loads(self):
        categoria = Categoria.objects.create(nombre="Novela")

        response = self.client.get(
            f"/catalogo/categorias/{categoria.pk}/editar/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario.html")
        self.assertContains(response, 'value="Novela"')

    def test_categoria_edit_updates_categoria(self):
        categoria = Categoria.objects.create(
            nombre="Novela", descripcion="Descripción anterior"
        )

        response = self.client.post(
            f"/catalogo/categorias/{categoria.pk}/editar/",
            {"nombre": "Ciencia ficción", "descripcion": "Actualizada"},
        )

        self.assertRedirects(response, "/catalogo/categorias/")
        categoria.refresh_from_db()
        self.assertEqual(categoria.nombre, "Ciencia ficción")
        self.assertEqual(categoria.descripcion, "Actualizada")

    def test_categoria_edit_returns_404_for_missing_categoria(self):
        response = self.client.get("/catalogo/categorias/999/editar/")

        self.assertEqual(response.status_code, 404)

    def test_libro_list_page_loads(self):
        categoria = Categoria.objects.create(nombre="Novela")
        Libro.objects.create(
            titulo="Don Quijote de la Mancha",
            autor="Miguel de Cervantes",
            fecha_publicacion="1605-01-16",
            categoria=categoria,
        )

        response = self.client.get("/catalogo/libros/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "libros/libros_list.html")
        self.assertContains(response, "Crear Nuevo Libro")
        self.assertContains(response, "16 de enero de 1605")
        self.assertContains(response, 'border="1"')
        self.assertContains(response, "Editar")
        self.assertContains(response, "Eliminar")

    def test_libro_create_page_loads(self):
        response = self.client.get("/catalogo/libros/crear/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "libros/formulario.html")
        self.assertContains(response, 'name="titulo"')
        self.assertContains(response, 'name="isbn"')

    def test_libro_form_creates_libro(self):
        categoria = Categoria.objects.create(nombre="Novela")

        response = self.client.post(
            "/catalogo/libros/crear/",
            {
                "titulo": "Cien años de soledad",
                "autor": "Gabriel García Márquez",
                "fecha_publicacion": "1967-06-05",
                "categoria": categoria.pk,
                "isbn": "9780307474728",
            },
        )

        self.assertRedirects(response, "/catalogo/libros/")
        self.assertTrue(
            Libro.objects.filter(
                titulo="Cien años de soledad",
                categoria=categoria,
                isbn="9780307474728",
            ).exists()
        )

    def test_libro_update_page_loads(self):
        categoria = Categoria.objects.create(nombre="Novela")
        libro = Libro.objects.create(
            titulo="Don Quijote",
            autor="Miguel de Cervantes",
            fecha_publicacion="1605-01-16",
            categoria=categoria,
        )

        response = self.client.get(f"/catalogo/libros/{libro.pk}/editar/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "libros/formulario.html")
        self.assertContains(response, "Don Quijote")

    def test_libro_delete_requires_confirmation_and_deletes_on_post(self):
        categoria = Categoria.objects.create(nombre="Novela")
        libro = Libro.objects.create(
            titulo="Don Quijote",
            autor="Miguel de Cervantes",
            fecha_publicacion="1605-01-16",
            categoria=categoria,
        )
        url = f"/catalogo/libros/{libro.pk}/eliminar/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "libros/confirm_delete.html")

        response = self.client.post(url)
        self.assertRedirects(response, "/catalogo/libros/")
        self.assertFalse(Libro.objects.filter(pk=libro.pk).exists())
