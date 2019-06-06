"""
$ python3 -m lexicographic.test_sequences
"""

import unittest
import random, itertools
from .sequences import Lexicographic

class LexicographicTest(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_failures(self):
        with self.assertRaises(ValueError):
            Lexicographic(0)
        with self.assertRaises(ValueError):
            Lexicographic(-1)
        with self.assertRaises(IndexError):
            Lexicographic(15)[16]
        with self.assertRaises(IndexError):
            Lexicographic(15)[-1]
        with self.assertRaises(ValueError):
            Lexicographic(15).index(-1)
        with self.assertRaises(ValueError):
            Lexicographic(15).index(16)
    
    def test_edgecases(self):
        pass
        
    def test_functional(self):
        for i in range(3):
            size = random.randint(1, 10**5)
            self.assertEqual(list(Lexicographic(size)), 
                             list(map(int, sorted(range(size+1), key=str))),
                             "{!r:} is Incorrect".format(Lexicographic(size))
                            )
                            
        L = Lexicographic(1015)
        for i in itertools.chain([10, 11, 100, 111, 99, 999, 1015], 
                                 random.sample(range(1015), k=10)):
            self.assertEqual(L[L.index(i)], i, i)
    
if __name__ == '__main__':
    unittest.main()
