import itertools
try:
    from math import gcd
except ImportError:
    from fractions import gcd

Limit = 10 ** 9 + 7
CoPrimePairs = {
    0: [],
    1: [(1, 1)],
    2: [(1, 1), (1, 2)],
    3: [(1, 1), (1, 2), (1, 3), (2, 3)],
    4: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)],
    5: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)],
    6: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 5),
        (3, 4), (3, 5),
        (4, 5),
        (5, 6),
       ],
    7: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
        (2, 3), (2, 5), (2, 7),
        (3, 4), (3, 5), (3, 7),
        (4, 5), (4, 7),
        (5, 6), (5, 7),
        (6, 7),
       ],
    8: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 3), (2, 5), (2, 7),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 5), (4, 7),
        (5, 6), (5, 7), (5, 8),
        (6, 7),
        (7, 8),
       ],
    9: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 5), (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7),
        (7, 8), (7, 9),
        (8, 9),
       ],
    10: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), 
        (1, 10),
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8), (3, 10),
        (4, 5), (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7),
        (7, 8), (7, 9), (7, 10),
        (8, 9),
        (9, 10),
       ],
}

def co_prime_pairs(n):
    # FIXME utiliz this and remove CoPrimePairs
    for pair in itertools.product(range(1, n+1), range(1, n+1)):
        if gcd(*pair) == 1:
            yield pair

def co_primes(n):
    """ returns list of co-primes for 1 to n """
    pairs = set()
    for pair in CoPrimePairs[n]:
        pairs.add(pair)
        pairs.add(pair[::-1])
    return [tuple(pair[1] for pair in pairs if pair[0] == i) for i in range(n+1)]
           
def ways(num, length):
    coprimes = co_primes(num)
    ways = [0] + [1] * num
    for _ in range(length):
        ways = [
            sum(map(ways.__getitem__, coprimes[i]))
            for i in range(num + 1)
        ]
    return ways[1] % Limit

if __name__ == '__main__':
    A = int(input("enter A, the runway length | 1 <= A <= 10\u2079: "))
    B = int(input("enter B, the number of runways | 0 <= B <= 10: "))
    
    assert 1 <= A <= 10 ** 9, "1 <= A <= 10\u2079"
    assert 1 <= B <= 10, "0 <= B <= 10"
    print (ways(B, A))
