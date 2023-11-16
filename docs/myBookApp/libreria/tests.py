from django.test import TestCase

# Create your tests here.
from libreria.models import Book,


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="The Lord of the Rings", author="J.R. Tolkien", genre="Aventura", description="Aventura mágica.", isbn="IS8729001")
        
    def test_get_book(self):
        """Testing get Book"""
        b1 = Book.objects.get(title="The Lord of the Rings")
    
        self.assertEqual(b1.title, 'The Lord of the Rings')

    def test_update_book(self):
        print("""Testing update Book""")
        b1 = Book.objects.get(title="Harry Potter and the Goblet of Fire")
        print("Get"+b1.title)
        b1.title="Harry Potter y el Cáliz de Fuego"
        print("Changing Title")
        b1.save()   
        b2 = Book.objects.get(title="Harry Potter y el Cáliz de Fuego")
        print("Get book updated"+b2.title)
        self.assertEqual(b2.title, 'Harry Potter y el Cáliz de Fuego')    