#!/usr/bin/python3

''' Class Square '''
class Square(object):
    ''' Square constructor '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    ''' Function area to calculate the area of the square '''
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size


    ''' property setter '''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
