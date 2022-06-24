from django.test import TestCase

from .models import Author, Book


class BookTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name = 'JRR',
            last_name = 'Tolkien'
        )


        self.book = Book.objects.create(
            title='The Hobbit',
            author= self.author,
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


class AuthorTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            first_name = 'JRR',
            last_name = 'Tolkien'
        )

    def test_author_listing(self):
        self.assertEqual(f'{self.author.first_name}', 'JRR')
        self.assertEqual(f'{self.author.last_name}', 'Tolkien')
