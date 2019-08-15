"""
$ ls VoerEir
__init__.py  __pycache__  singletonref.py  test.py
$ python3 -m VoerEir.test
"""

import unittest
import gc

from .singletonref import Singleton
from .decorators import sum
from .substrings import lds
from .factorys import Shape, Circle, Square

class AssessmentTest(unittest.TestCase):

    def setUp(self):
        pass    
    
    def test_singleton(self):
        instance1 = Singleton()
        instance2 = Singleton()
        self.assertIs(instance1, instance2, "Singleton is buggy!")

    def test_sum(self):
        self.assertEqual(sum(1, 1), '** 2 3', "buggy @starify")
        self.assertEqual(sum(12, 10), sum(10, 12), "sum() is not a symmetric operator!")
        self.assertNotEqual(sum(0, 0), '', "it is actually ' 0 1'")
        
    def test_lds(self):
        cases = [("defaasdf", 'defa'),
                ("aaaaaaaaaa", 'a'),
                ("grijesh", 'grijesh'),
                ("VoerEir", 'VoerEi'),
                ("defaasdfxyw0123", 'asdfxyw0123'),
                ("defaasdfxyw0123aaa", 'asdfxyw0123'),
                ("", ''),
                ]
        for string, substring in cases:
            self.assertEqual(lds(string), substring, f"lds('{string}') != '{substring}'")
            
    def test_shape(self):
        for shapename, cls in [('circle', Circle),
                               ('Square', Square),
                              ]:    
            self.assertIsInstance(Shape.factory(shapename), cls, "Bug in Shape()")
            
    def test_failures(self):
        with self.assertRaises(ValueError):
            Shape.factory('NewShape')
            
    def test_for_new_shape(self):
        NewShape = type('NewShape', (Shape, ), {})
        self.assertIsInstance(Shape.factory('NewShape'), NewShape, "Bug in Shape")
        del NewShape
        gc.collect()
        with self.assertRaises(ValueError):
            Shape.factory('NewShape')
        
if __name__ == '__main__':
    unittest.main()
