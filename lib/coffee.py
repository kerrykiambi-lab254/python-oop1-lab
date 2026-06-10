#!/usr/bin/env python3

class Coffee:
    """
    A class representing a coffee item in the bookstore.
    """
    def __init__(self, size, price):
        """
        Initialize a new Coffee instance.
        """
        self.size = size
        self.price = price

    @property
    def size(self):
        """
        Get the size of the coffee.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the coffee, ensuring it's Small, Medium, or Large.
        """
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """
        Print a message and increase the price of the coffee by 1.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1