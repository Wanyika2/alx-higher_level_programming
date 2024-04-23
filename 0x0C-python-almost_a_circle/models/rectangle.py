# models/rectangle.py
from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance with width, height, x, y, and id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.__y = value

if __name__ == "__main__":
    # Test the Rectangle class
    rect = Rectangle(10, 20, 1, 2, 100)
    print("Rectangle ID:", rect.id)        # Should print 100
    print("Rectangle Width:", rect.width)  # Should print 10
    print("Rectangle Height:", rect.height)  # Should print 20
    print("Rectangle X:", rect.x)          # Should print 1
    print("Rectangle Y:", rect.y)          # Should print 2
