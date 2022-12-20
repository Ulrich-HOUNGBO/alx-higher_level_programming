#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size and validates size
"""
class Square:
    """
    class Square definitions

    Args:
        size: size of a side in square
    """
    def __init__(self,size):
        """
        Initialize square

        Args:
            size (_type_): size of a side in square
        """
        if size is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

