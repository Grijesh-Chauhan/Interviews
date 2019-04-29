# note: my solution below is not the best by complexity 
# please check https://stackoverflow.com/q/251781/1673391

import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

def nth_largest(n, numbers):
    numbers = sorted(numbers, reverse=True)
    nlarges = take(n, itertools.groupby(numbers))
    if len(nlarges) < n:
        return
    return nlarges[-1][0]
    
if __name__ == '__main__':
    assert nth_largest(3, []) is None
    assert nth_largest(3, [1, 2]) is None
    assert nth_largest(2, [5, 5, 2, 2, 1, 1, 2.5 ]) == 2.5
    assert nth_largest(3, [5, 5, 2, 2, 1, 1, 2.5 ]) == 2
    assert nth_largest(1, [5, 5, 2, 2, 1, 1, 2.5 ]) == 5
    assert nth_largest(3, [1, 1, 1, 1, 0]) is None
    assert nth_largest(1, [1, 1, 1, 1]) == 1
    assert nth_largest(2, [1, 1, 1, 1]) is None
    
    
# if all numbers are unique or if question is releax that 2th larg in [1, 1] = 1
# then heapq module, `heapq.nlargest` and `heapq.nsmallest` are very helpful
#
#        import heapq
#        def nth_largest(n, numbers):
#            return heapq.nlargest(n, numbers)[-1]
#
#
#        >> iterable = (ord(c) for c in 'grijesh')
#        >> sorted(iterable)
#        .. [101, 103, 104, 105, 106, 114, 115]
#        >> nth_largest(4, (ord(c) for c in 'grijesh'))
#        .. 105
#
#
# Python Cookbook:
# The nlargest() and nsmallest() functions are most appropriate if you are trying
# to find a relatively small number of items. If you are simply trying to find the
# single smallest or largest item (N=1), it is faster to use min() and max().
# Similarly, if N is about the same size as the collection itself, it is usually
# faster to sort it first and take a slice (i.e., use sorted(items)[:N] or 
# sorted(items)[-N:] ).


