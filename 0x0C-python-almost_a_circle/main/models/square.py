#!/usr/bin/python3
from models.rectangle import Rectangle
"""Represent a square class that inherit rectangle"""
# Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """define square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing square class
        Args:
            size: size of the square
            x: x co-ordinate of the square
            y: y co-ordinate of the square
            id: indentify of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size"""
        # if type(value) is not int:
        #     raise TypeError("width must be an integer")
        # if value <= 0:
        #     raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the Square

        Args:
            *args: new values
                - 1st = id
                - 2nd = size
                - 3rd = x
                - 4th = y
        kwargs: new key pair value

        """
        if args is not None and kwargs is not None:
            if args:
                for idx, value in enumerate(args):
                    match idx:
                        case 0:
                            self.id = value
                        case 1:
                            self.size = value
                        case 2:
                            self.x = value
                        case 3:
                            self.y = value
            elif kwargs:
                for key, value in kwargs.items():
                    match key:
                        case 'id':
                            self.id = value
                        case 'size':
                            self.size = value
                        case 'x':
                            self.x = value
                        case 'y':
                            self.y = value
            return
        return self.__init__(self.size,
                             self.x, self.y)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def __str__(self):
        """string representation of the square"""
        result = f'[{Square.__name__}] ({self.id}) '
        result += f'{self.x}/{self.y} - {self.width}'
        return result
