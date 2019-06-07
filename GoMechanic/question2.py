import itertools
try:
    from math import gcd
except ImportError:
    from fractions import gcd

# FIXME may be use limit to fix runtime for larger runway lenght!
Limit = 10 ** 9 + 7

def coprime_pairs(n):
    for pair in itertools.product(range(1, n+1), range(1, n+1)):
        if gcd(*pair) == 1:
            yield pair
            
def ways(num, length):
    coprimes = [tuple(pair[1] for pair in [*coprime_pairs(num)] if pair[0] == i)
                for i in range(num+1)
               ]
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
