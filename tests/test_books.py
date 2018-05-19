#  test_book.py
import unittest
import json
import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.config_tests import ConfigTestCase


class BooksEndPoint(ConfigTestCase):
    """This class represents the books test case"""

    def test_add_book(self):
        """Test API can create a book (POST request)"""
        response = self.client().post('/api/v2/books', data=json.dumps(self.books),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("book created", str(response.data))

    def test_get_book(self):
        """Test API can create get all books (GET request)"""
        response = self.client().get('/api/v2/books')
        self.assertEqual(response.status_code, 200)

    def test_get_one_book(self):
        """Test API can get one book (GET request)"""
        response = self.client().get('/api/v2/books/1')
        self.assertEqual(response.status_code, 200)

    def test_modify_book(self):
        book_title = {"title": "Harry"}
        book_author = {"author": "Joanne Rowling"}
        book_copies = {"copies": 4}
        """Test API can modify book (PUT request)"""
        response = self.client().put('/api/v2/books/1', data=json.dumps(book_title), content_type='application/json')
        response1 = self.client().put('/api/v2/books/1', data=json.dumps(book_author), content_type='application/json')
        response2 = self.client().put('/api/v2/books/1', data=json.dumps(book_copies), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_delete_book(self):
        """Test API can delete book (DELETE request)"""
        response = self.client().delete('/api/v2/books/1')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
