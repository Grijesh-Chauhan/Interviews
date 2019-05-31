class Stack(list):
    
    def push(self, item):
        self.append(item)

    def top(self):
        return self[-1]
        
    def size(self):
        return len(self)
    
    def isempty(self):
        """ if stack.isemplty():
                do somethings...

            or

            if not stack:
                do somethings...
        """
        return self.size() == 0

    def __iter__(self):
        """ iter in lifo """
        return super(Stack, self).__reversed__()
        
    def __reversed__(self):
        return super(Stack, self).__iter__()
        
    def popall(self):
        try:
            while True:
                yield self.pop()
        except IndexError:
            pass
        
    def clear(self):
        del self[:]

    def __repr__(self):
        if not self:
            return '%s()' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, super(Stack, self).__repr__())
