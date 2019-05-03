"""
Given an array of integers(positive or negative), print the next greater element
of all elements in the array. If there is no greater element then print None.
"""
import itertools
import container

def yieldNGEpairs(array):
    """ Generates next greater elements """
    stack = container.Stack()
    
    def lessthan(element):
        def predicate(top):
            if top < element:
                return True
            stack.push(top)
            return False
        return predicate
    
    for element in array:
        if stack.isempty() or stack.top() > element:
            stack.push(element)
            continue
                    
        for item in itertools.takewhile(lessthan(element), stack.popall()):
            yield item, element
        stack.push(element)

    for item in stack.popall():
        yield item, None


if __name__ == '__main__':
    for array in  [40, 50, 11, 32, 55, 68, 75],\
                  [98, 23, 54, 12, 20, 7, 27]:
        print("\n")
        print(array)
        for pairs in yieldNGEpairs(array):
            print(pairs)
