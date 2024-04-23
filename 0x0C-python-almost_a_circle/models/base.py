# models/base.py

class Base:
    """Base class for managing id attribute."""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with id attribute."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    # Test the Base class
    obj1 = Base()
    print("Object 1 id:", obj1.id)  # Should print 1

    obj2 = Base()
    print("Object 2 id:", obj2.id)  # Should print 2

    obj3 = Base(100)
    print("Object 3 id:", obj3.id)  # Should print 100
