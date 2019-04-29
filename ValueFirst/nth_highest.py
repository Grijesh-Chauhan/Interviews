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
