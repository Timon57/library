from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Django for APIs",
            subtitle = "Build web APIs with Python and Django",
            author = "Timon",
            isbn = "1234"
        )
    def test_api_listView(self):
        response = self.client.get(reverse("book_list"))# checks the url name
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(),1)
        self.assertContains(response,self.book)
