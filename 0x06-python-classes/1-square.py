#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""
class Square:
    """
    class Square definitions
    
    Args:
        size: size of a side in square
    """
    def __init__(self,size) -> None:
        """
        Initialize square

        Args:
            size (_type_): size of a side in squar
        """
        self.__size = size
