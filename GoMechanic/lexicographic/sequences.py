from .containers import Stack

class Lexicographic:
    """
    Lexicographic sequence are numbers from 1 to size in lexicographic order e.g.

    >> list(Lexicographic(11)) => [0, 1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    >> L = Lexicographic(112)
    >> L[1], L[2], L[3], L[4], L[5] => (1, 10, 100, 101, 102)
    >> L.index(99) => 112
    >> L.index(112) => 16
    """
    def __init__(self, size):
        if size < 1:
            raise ValueError("size should be > 0")
        self.size = size

    def distance(self, number):
        """returns number of numbers between 'number' and 'number + 1'
        """
        nodes = 0
        leftend, rightend = number, number + 1
        while leftend <= self.size:
            nodes += min(self.size + 1, rightend) - leftend
            leftend *= 10
            rightend *= 10
        return nodes
        
    def __getitem__(self, index):
        if index == 0:
            return 0
        if index < 0 or index > self.size:
            raise IndexError("lex index out of range")
                
        curtindex, number = 1, 1
        while curtindex < index:
            delta = self.distance(number)
            if delta <= index - curtindex:
                curtindex += delta
                number += 1 # travel in same level increase by +1
            else:
                curtindex += 1
                number *= 10 # travel in next depth level increase by *10
        return number
        
    def __iter__(self):
        return IterLexicographic(self.size)
        
    def index(self, number):
        if number < 0 or number > self.size:
            raise ValueError("{!r:} not in {!r:}".format(number, self))
        if number == 0:
            return 0
        digits = []
        while number:
            number, remainder = divmod(number, 10)
            digits.insert(0, remainder)
        curt, index = 1, 0
        for digit in digits:
            index += 1
            for _ in range(digit-1 if curt == 1 else digit): # 0 has nine childs, other has 10
                index += self.distance(curt)
                curt += 1
            curt *= 10
        return index
                    
    def __repr__(self):
        return "{name}({size})".format(name=self.__class__.__name__,
                                       size=self.size)
                                       
class IterLexicographic:
    """ `IterLexicographic(n) == iter(Lexicographic(n))`
    """
    def __init__(self, size):
        self.stack = Stack()
        self.size = size
        self.curt = 0
        self.stopflag = False

    def __next__(self):
        if self.curt == 0:
            self.curt = 1
            return 0
        curt = self.curt
        if (curt + 1) % 10 and curt + 1 <= self.size:
            self.stack.push(curt + 1)
        if curt * 10 <= self.size:
            self.curt = curt * 10
        elif not self.stack.isempty():
            self.curt = self.stack.pop()
        elif self.stopflag:
            raise StopIteration
        else:
            # Python do not have Go's like defer stm!
            self.stopflag = True
        return curt
        
    next = __next__
