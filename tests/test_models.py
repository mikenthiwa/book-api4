import unittest
from app.models import Books, Users


class BooksTest(unittest.TestCase):
    def setUp(self):
        self.book = Books()
        self.user = Users()

    def test_get_books_method(self):
        """Testing get all book method"""

        result = self.book.get_books()
        self.assertEqual(result, {1: [{"Title": "Harry Potter and Chamber of Secrets",
                                       "Author": "J.K Rowling", "Copies": 2}],
                                  2: [{"Title": "Lone Wolf",
                                       "Author": "David Archer", "Copies": 3}]})

    def test_get_specific_book_method(self):
        """Testing get a book method"""

        # When book id is int
        book_id = 1
        result = self.book.get_book(book_id)
        self.assertEqual(result, [{"Title": "Harry Potter and Chamber of Secrets",
                                   "Author": "J.K Rowling",
                                   "Copies": 2}])

    def test_post_book_method(self):
        """Testing post a book method"""

        book_id = 4
        title = "The Whistler"
        author = "John Grisham"
        copies = 3
        result = self.book.post_book(book_id, title, author, copies)
        self.assertEqual(result, [{"Title": "The Whistler",
                                   "Author": "John Grisham", "Copies": 3}])

    def test_details(self):
        """Testing function details"""

        book_id = 1
        result = self.book.get_books()[book_id][0]
        self.assertEqual(result, {"Title": "Harry Potter and Chamber of Secrets",
                                  "Author": "J.K Rowling", "Copies": 2})

    def test_modify_book_title_method(self):
        """Testing modify book information"""

        # modify book title
        book_id = 2
        book_title = "Lost Girl"
        result = self.book.modify_book_title(book_id, book_title)
        self.assertEqual(result, [{"Title": "Lost Girl",
                                   "Author": "David Archer",
                                   "Copies": 3}])

        # modify book author
        book_author = "Paulo Coelho"
        result = self.book.modify_book_author(2, book_author)
        self.assertEqual(result, [{"Title": book_title,
                                   "Author": book_author,
                                   "Copies": 3}])

        # modify book copies
        copies = 5
        result = self.book.modify_book_copies(book_id, copies)
        self.assertEqual(result, [{"Title": book_title,
                                   "Author": book_author,
                                   "Copies": copies}])

    def test_delete_method(self):
        """Testing delete method"""

        book_id = 2
        all_books = self.book.get_books()
        self.book.delete_book(book_id)
        self.assertNotIn(book_id, all_books.keys())

    def test_get_users_method(self):
        """Testing get all users method"""

        result = self.user.get_users()
        self.assertTrue(result)

    def test_register_user_method(self):
        """Test register user method"""

        username = "regina.nthiwa"
        email = "reg@gmail.com"
        password = 123456789
        result = self.user.add_user(username, email, password)
        self.assertEqual(result, [{"Email": email,
                                   "Password": password}])


if __name__ == '__main__':
    unittest.main()
