#!/usr/bin/env python3

class Book:
    """
    A class representing a book in the bookstore.
    """
    def __init__(self, title, page_count):
        """
        Initialize a new Book instance.
        """
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """
        Get the page count of the book.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Set the page count of the book, ensuring it's an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """
        Print a message indicating a page has been turned.
        """
        print("Flipping the page...wow, you read fast!")