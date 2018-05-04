#!/usr/bin/python3
class Square(): 
    ''' Square class '''
    
    ''' constructor '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    ''' Calculates the area '''    
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        ''' property setter '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        ''' property setter '''
        if isinstance(value, tuple) and len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        ''' prints in stdout the square with the character # '''
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
                print()
        for col in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
