class Shape:

    @classmethod    
    def factory(cls, shapename: "name of Shape subclass") -> "subclass instance":
        for aclass in cls.__subclasses__():
            # although Python is case sensitive language, but shape names
            if aclass.__name__.lower() == shapename.lower():
                return aclass()
        else:
            raise ValueError(f"Invalid shape name, {shapename!r} ")
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"

class Circle(Shape):
    """ use `Shape.factory('Circle')` instead of `Circle()` """

class Square(Shape):
    """ use `Shape.factory('Square')` instead of `Square()` """
