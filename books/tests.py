from django.test import TestCase

from django.urls import reverse

from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "DwDm",
            subtitle = "Data",
            author = "Bhup saud",
            isbn = '19837249812',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "DwDm")
        self.assertEqual(self.book.subtitle, "Data")
        self.assertEqual(self.book.author, "Bhup saud")
        self.assertEqual(self.book.isbn, "19837249812")

    def test_book_listView(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Data")
        self.assertTemplateUsed(response, "books/book_list.html")


