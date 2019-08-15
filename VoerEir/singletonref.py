"""
a reference implementation of creating singleton class
"""

# clarification: to create an instance we call class as function call
# instance = Class()
# In `SingleTonType`, we intercept instance creation by overriding `__call__`
# of `type` function. Because we knows, `type` is factory to create classes
# in Python and a class is a callable object itself

class SingletonType(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__instance = None
        
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance

class Singleton(metaclass=SingletonType):
    """only one instance of Singleton class can be created"""
    pass
