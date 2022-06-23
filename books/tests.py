from django.test import TestCase

from .models import Book


class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='The Hobbit',
            author='JRR Tolkien',
            publisher='Test Publisher',
            publication_date='1985-01-01',
            price='25.00',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'The Hobbit')
        self.assertEqual(f'{self.book.author}', 'JRR Tolkien')
        self.assertEqual(f'{self.book.publisher}', 'Test Publisher')
        self.assertEqual(f'{self.book.publication_date}', '1985-01-01')
        self.assertEqual(f'{self.book.price}', '25.00')
