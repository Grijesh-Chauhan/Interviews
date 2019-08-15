class Shape:
    @classmethod    
    def factory(cls, shapename):
        for aclass in cls.__subclasses__():
            # although Python is case sensitive language, shape name
            if aclass.__name__.lower() == shapename.lower():
                return aclass()
        else:
            raise ValueError(f"{shapename} invalid shape name")
    
    def __str__(self):
        return "{}()".format(self.__class__.__name__)

class Circle(Shape):
    pass
        
class Square(Shape):
    pass
