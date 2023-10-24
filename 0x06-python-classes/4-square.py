#!/usr/bin/python3
# 0-square.py by Abdirahman Abdi
"""A module that defines a square"""


class Square:
    """A class that represents a square"""

    def __init_(self, size=0):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
           TypeError: if size is not longer
           ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('Size must be an integer')
        if size < 0:
            raise ValueError('Size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('Size must be an integer')
        if value < 0:
            raise ValueError('Size must be >= -0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return(self.__size ** 2)
