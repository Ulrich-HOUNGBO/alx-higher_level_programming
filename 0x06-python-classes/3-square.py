#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size and public attribute area
"""
class Square:
    """
    class Square definitions

    Args:
        size(int): size of a side in square
    """
    def __init__(self,size = 0):
        """
        Initialize square

        Args:
            __size (int): size of a side of square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculate area of square

        Returns:
            area: area of square
        """
        return (self.__size)**2


