#!/usr/bin/python3
""""""
Base = __import__('base.py').Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be a integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be a integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be a integer")

        if value <= 0:
            raise ValueError("x must be > 0")

        self.x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("x must be a integer")

        if value <= 0:
            raise ValueError("x must be > 0")

        self.y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        return "[{:s}] ({:d}) {:d} / {:d} - {:d} / {:d}".format(self.__class__.name, self.id, self.__x,
                                                                self.__y, self.__width, self.__height)
