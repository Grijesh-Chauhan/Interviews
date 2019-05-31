"""
Given an array of integers(positive or negative), print the next greater element
of all elements in the array. If there is no greater element then print None.
"""
# https://www.geeksforgeeks.org/next-greater-element/
# Hint:
# The nested loop solution in which for each outer-loop number we find 
# the greater number in inner loop.
# 
# Rather than nested loop solution the trick in below implementation -> stacks sub
# -array that appears in decreasing order, and as first greater number comes pop-all
# 
# e.g.   2,  45, 13, 7, 4, 2, 9, 10, 65
#            ^---stack-----^  ^
#                             | for 9 pop-all until before 13
#
import itertools
import container

def yieldNGEpairs(array):
    """ Generates next greater elements """
    stack = container.Stack()
    
    def lessthan(element):
        """prevent the top (> element) loss"""
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
                    
        for top in itertools.takewhile(lessthan(element), stack.popall()):
            yield top, element
        stack.push(element)

    for top in stack.popall():
        yield top, None


if __name__ == '__main__':
    for array in  [40, 50, 11, 32, 55, 68, 75],\
                  [98, 23, 54, 12, 20, 7, 27]:
        print("\n")
        print(array)
        for pairs in yieldNGEpairs(array):
            print(pairs)
